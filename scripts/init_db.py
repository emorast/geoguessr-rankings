import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    
    # Create tables
    cur.execute('''DROP TABLE IF EXISTS players_results''')
    cur.execute('''
                CREATE TABLE players_result(
                user_id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                date TEXT,
                game_token TEXT,
                total_score INTEGER,  
                score_1 TEXT,
                score_2 TEXT,
                score_3 TEXT,
                score_4 TEXT,
                score_5 TEXT  
                )''')
    
    cur.execute('''DROP TABLE IF EXISTS played_maps''')
    cur.execute('''
                CREATE TABLE played_maps(
                map_name TEXT PRIMARY KEY,
                game_token TEXT,
                location_1 TEXT,
                location_2 TEXT,
                location_3 TEXT,
                location_4 TEXT,
                location_5 TEXT             
                )''')
    
    conn.close()
    
    

