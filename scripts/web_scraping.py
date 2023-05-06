import requests
from bs4 import BeautifulSoup
from config import *
import pickle
import json
import sqlite3


def save_session(session):
    with open("save.pkl", "wb") as f:
        pickle.dump(session, f)


def load_session():
    with open("save.pkl", "rb") as f:
        return pickle.load(f)


def get_request(session, url):
    req = session.get(url)
    return BeautifulSoup(req.content, "html.parser")


def get_stats(session, data):
    # Connect to db
    conn = sqlite3.connect(os.path.join(DATA_DIR, "db.sqlite3"))
    cur = conn.cursor()

    # Fetch creation date for timestamp
    creation_info = data.find_all("p", class_="league-details__created")
    date = str(creation_info[0].text.split(",")[1]).strip()

    # Fetch data
    legs = data.find_all("div", class_="leg-list__leg")
    if len(legs) != 0:
        for leg in legs:
            game_token = leg.a["href"].split("/")[-1]
            api_url = (
                main_url
                + "/api/v3/results/highscores/"
                + game_token
                + "?friends=false&limit=50"
            )
            json_data = json.loads(get_request(session, api_url).text)

            # Get map information
            info = json_data["items"][0]["game"]
            map_name = info["mapName"]

            # Insert game information
            try:
                to_insert = (game_token, map_name, date)
                cur.execute("INSERT INTO games VALUES(?, ?, ?)", to_insert)
                conn.commit()

                # Insert locations
                for location in info["rounds"]:
                    location_id = location["panoId"]
                    lat = float(location["lat"])
                    lng = float(location["lng"])

                    to_insert = (location_id, map_name, game_token, date, lat, lng)
                    cur.execute(
                        "INSERT INTO locations VALUES(?, ?, ?, ?, ?, ?)", to_insert
                    )
                conn.commit()

                # Insert player stats
                for player in json_data["items"]:
                    full_name = player["playerName"]
                    user_id = player["userId"]
                    total_score = int(player["totalScore"])
                    rounds = player["game"]["player"]["guesses"]
                    score_by_round = []
                    for round in rounds:
                        score_by_round.append(int(round["roundScore"]["amount"]))

                    # Insert new players in database if any
                    try:
                        to_insert = (user_id, full_name, 0, 1000, 1000, None)
                        cur.execute(
                            "INSERT INTO players VALUES(?, ?, ?, ?, ?, ?)", to_insert
                        )
                        conn.commit()
                        print("Added %s (%s)" % (full_name, user_id))
                    except:
                        pass

                    to_insert = (
                        user_id,
                        full_name,
                        date,
                        game_token,
                        total_score,
                        score_by_round[0],
                        score_by_round[1],
                        score_by_round[2],
                        score_by_round[3],
                        score_by_round[4],
                    )
                    cur.execute(
                        "INSERT INTO results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        to_insert,
                    )
            except Exception as e:
                print(e)
                print("Error: Results from %s are already imported" % game_token)
    conn.close()


def web_scrape(league_url):
    print("Scraping: %s" % league_url)
    with requests.session() as session:
        if login_required:
            res = session.post(
                login_url, json={"email": email, "password": password}, headers=headers
            )
            if res.status_code == 200:
                print("Successful login")
                save_session(session=session)
            else:
                print("Error: Unable to connect")
        else:
            session = load_session()

        get_stats(session, get_request(session, league_url))
