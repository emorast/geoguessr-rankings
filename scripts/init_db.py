import sqlite3
from config import DB

if __name__ == "__main__":
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Create tables
    cur.execute("""DROP TABLE IF EXISTS games""")
    cur.execute(
        """          
                    CREATE TABLE games(
                        game_token TEXT PRIMARY KEY NOT NULL,
                        map_name TEXT,
                        date DATE
                    )"""
    )
    cur.execute(
        """
                CREATE UNIQUE INDEX idx_game_token ON games (game_token)
                """
    )

    cur.execute("""DROP TABLE IF EXISTS players""")
    cur.execute(
        """  
                CREATE TABLE players(
                    user_id TEXT PRIMARY KEY NOT NULL,
                    full_name TEXT,
                    played_games INTEGER,
                    overall_elo INTEGER,
                    seasonal_elo INTEGER,
                    weekly_rank INTEGER                
                )"""
    )
    cur.execute(
        """
                CREATE UNIQUE INDEX idx_user_id ON players (user_id)
                """
    )
    cur.execute("""DROP TABLE IF EXISTS results""")
    cur.execute(
        """ 
                CREATE TABLE results(
                    user_id TEXT,
                    full_name TEXT,
                    date DATE,
                    game_token TEXT,
                    total_score INTEGER,  
                    score_1 INTEGER,
                    score_2 INTEGER,
                    score_3 INTEGER,
                    score_4 INTEGER,
                    score_5 INTEGER  
                )"""
    )
    cur.execute(
        """
                CREATE INDEX idx_results ON results (user_id, date, game_token)
                """
    )

    cur.execute("""DROP TABLE IF EXISTS locations""")
    cur.execute(
        """               
                CREATE TABLE locations(
                    location TEXT,
                    map_name TEXT,
                    game_token TEXT,
                    date DATE,
                    lat FLOAT,
                    lng FLOAT 
                )"""
    )
    cur.execute("""DROP TABLE IF EXISTS elo""")
    cur.execute(
        """               
                CREATE TABLE elo(
                    user_id TEXT,
                    date DATE,
                    elo INTEGER
                )"""
    )
    cur.execute(
        """
                CREATE INDEX idx_elo ON elo (user_id, elo)
                """
    )

    conn.close()
