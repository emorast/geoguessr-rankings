import requests
from bs4 import BeautifulSoup
from config import *
import pickle

def save_session(session):
    with open('save.pkl', 'wb') as f:
        pickle.dump(session, f)

def load_session():
    with open('save.pkl', 'rb') as f:
        return pickle.load(f)
            
def get_leg_results(data):
    legs = data.find_all('div', class_ = "leg-list__leg")
    if len(legs) !=0:
        for leg in legs:
            print(leg)

if __name__ == '__main__':
    with requests.session() as session:
        if login_required:
            res = session.post(login_url, json={
                "email": email,
                "password": password},
                headers=headers)
            if res.status_code == 200:
                print("Successful login")
                save_session(session=session)
            else:
                print("Error: Unable to connect")           
        else:
            session = load_session()
                
        req = session.get(league_url)
        data = BeautifulSoup(req.content, 'html.parser')
        
        get_leg_results(data)
        
        
        
        

