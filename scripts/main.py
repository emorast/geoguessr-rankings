from web_scraping import *

if __name__ == '__main__':
    
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            web_scrape(line.strip())
        
    
    pass