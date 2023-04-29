import requests
from bs4 import BeautifulSoup
from config import *

def get_data_from_url(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')

def login_handler(data):
    
    tag = data.find_all('a', class_="button_link__xHa3x button_variantPrimary__xc8Hp")
    login_url = url + str(tag[0].get('href'))

def parse_data(data):
    
    leg_list = data.find_all('div', class_="leg-list__leg")
    if len(leg_list) != 0:
        for leg in leg_list:
            print(leg)
            
    else:
        login_handler(data)
        
if __name__ == '__main__':
    
    data = get_data_from_url(league_url)
    
    parse_data(data)