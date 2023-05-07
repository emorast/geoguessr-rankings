from web_scraping import *

"""
 Main-function
"""

if __name__ == "__main__":
    # Webscrape all urls in input.txt
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            web_scrape(line.strip())

    # Check the last time the ELO was calculated
