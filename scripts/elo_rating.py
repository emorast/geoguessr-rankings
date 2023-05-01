import sqlite3
from config import K, D, ALPHA

conn = sqlite3.connect('data.db')
cur = conn.cursor()

# Get list of all played games
# TODO extend functionality so games between certain dates can be selected
def get_games():
    res = cur.execute('''SELECT game_token FROM games''').fetchall()
    games = [x for x in res]     
    return games

# Function calculates and update
def calculate_elo(results, players):
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
                x = 1/(1+pow(10, ((elo_b-elo)/D)))
                expected_score += x
        
        expected_score = expected_score/(n_players*(n_players-1)/2)
        
        # Actual score
        sum = 0
        for i in range(1,n_players+1):
            sum += (pow(ALPHA, n_players-i)-1)
        actual_score = (pow(ALPHA, n_players-placement)-1)/sum
        new_elo = round(elo + K*(n_players-1)*(actual_score-expected_score))
        
        # Update ELO
        cur.execute('''UPDATE players SET overall_elo = ? WHERE user_id = ? ''', (new_elo,player[0]))
        
        # Update played_games
        res = cur.execute('''SELECT played_games FROM players WHERE user_id = ?''', (player[0],)).fetchall()
        played_games = res[0][0] + 1
        cur.execute('''UPDATE players SET played_games = ? WHERE user_id = ? ''', (played_games, player[0]))
        conn.commit()

if __name__ == '__main__':
    games = get_games()
    for game in games:
        res = cur.execute('''SELECT user_id, total_score FROM results WHERE game_token = ? ''', game)
        results = [x for x in res]
        players = {}
        for player_id in results:
            res = cur.execute('''SELECT user_id, overall_elo FROM players WHERE user_id = ? ''', (player_id[0],)).fetchall()
            id, elo = res[0]
            players[id] = elo
              
        calculate_elo(results, players)      
    
    conn.close()