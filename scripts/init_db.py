import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    
    # Create tables
    cur.execute('''DROP TABLE IF EXISTS games''')
    cur.execute('''          
                    CREATE TABLE games(
                        game_token TEXT PRIMARY KEY,
                        map_name TEXT,
                        date DATE
                    )''')
    cur.execute('''DROP TABLE IF EXISTS players''')
    cur.execute('''  
                CREATE TABLE players(
                    user_id TEXT PRIMARY KEY,
                    full_name TEXT,
                    played_games INTEGER,
                    overall_elo INTEGER,
                    seasonal_elo INTEGER,
                    weekly_rank INTEGER                
                )''')
    cur.execute('''DROP TABLE IF EXISTS results''')
    cur.execute(''' 
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
                )''')
    cur.execute('''DROP TABLE IF EXISTS locations''')
    cur.execute('''               
                CREATE TABLE locations(
                    id TEXT PRIMARY KEY,
                    map_name TEXT,
                    game_token TEXT,
                    date DATE,
                    lat FLOAT,
                    lng FLOAT 
                )''')   
    conn.close()
    
    

