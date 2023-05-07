import sqlite3
from config import K, D, ALPHA, DB


# Function calculates and update
def calculate_elo(game_token):
    conn = sqlite3.connect(DB)

    cur = conn.cursor()
    res = cur.execute(
        """SELECT user_id, total_score FROM results WHERE game_token = ? """, game_token
    )
    results = [x for x in res]
    players = {}
    for player_id in results:
        res = cur.execute(
            """SELECT user_id, overall_elo FROM players WHERE user_id = ? """,
            (player_id[0],),
        ).fetchall()
        id, elo = res[0]
        players[id] = elo

    n_players = len(results)
    results.sort(key=lambda tup: tup[1], reverse=True)

    for i, player in enumerate(results):
        elo = players[player[0]]
        placement = i + 1

        # Expected score
        expected_score = 0
        for other_player in results:
            elo_b = players[other_player[0]]
            if player[0] != other_player[0]:
                x = 1 / (1 + pow(10, ((elo_b - elo) / D)))
                expected_score += x

        expected_score = expected_score / (n_players * (n_players - 1) / 2)

        # Actual score
        sum = 0
        for i in range(1, n_players + 1):
            sum += pow(ALPHA, n_players - i) - 1
        actual_score = (pow(ALPHA, n_players - placement) - 1) / sum
        new_elo = round(elo + K * (n_players - 1) * (actual_score - expected_score))

        # Save current ELO rating

        # Update ELO
        cur.execute(
            """UPDATE players SET overall_elo = ? WHERE user_id = ? """,
            (new_elo, player[0]),
        )

        # Update played_games
        res = cur.execute(
            """SELECT played_games FROM players WHERE user_id = ?""", (player[0],)
        ).fetchall()
        played_games = res[0][0] + 1
        cur.execute(
            """UPDATE players SET played_games = ? WHERE user_id = ? """,
            (played_games, player[0]),
        )
        conn.commit()
        conn.close()
