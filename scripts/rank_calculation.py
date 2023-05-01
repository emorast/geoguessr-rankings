import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    
    # Get list of all players
    res = cur.execute('''SELECT user_id FROM players''').fetchall()
    players = [x for x in res]
    
    # Calculate win-loses
    
    res = cur.execute('''SELECT game_token, total_score FROM results WHERE user_id= ? ''', players[0] )
    for x in res:
        print(x)
    conn.close()