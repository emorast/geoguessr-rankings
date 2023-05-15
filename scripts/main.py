from web_scraping import *
from elo_rating import update_elo
from config import *

"""
 Main-function
"""
conn = sqlite3.connect(DB)
cur = conn.cursor()

if __name__ == "__main__":
    # Webscrape all urls in input.txt
    if shouldScrape:
        with open("input.txt") as f:
            lines = f.readlines()
            for line in lines:
                web_scrape(line.strip())

    res = cur.execute(
        """ SELECT game_token, date FROM games
        ORDER BY
            date ASC            
                      """
    ).fetchall()
    results = [x for x in res]

    for info in results:
        print(info)
        update_elo(info, cur)
    conn.commit()
    conn.close()
