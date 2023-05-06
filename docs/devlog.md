# geoguessr-elo Devlog
### 2023/05/06
- Added Bootstrap 5 framework
- Added home-page based on this [template](https://startbootstrap.com/previews/one-page-wonder)
- Changed the theme to more green-ish


### 2023/05/01
- Added tables *locations*, *maps*, *players* and *results* to the database
- Finishing the script for scraping league results into the database
- Started implementing elo rating system
### 2023/04/30
- Solved login problem. Instead of giving `requests.session().post()` the *payload* as a dict, a `.json`is given instead
- Solved problem with too many POST requests resulting in getting blocked from Geouessr.com
- Implemented scraping of the highscore-board from each leg in a league
- Added `sqlite`database connection
- Started `Django` project

### 2023/04/29
- Working with the mockup for the application and figuring out what functionality would be implemented in the first version. To its core, the *geoguesr-elo* application have to be able to
    - scrape results from [GeoGuessr](https://www.geoguessr.com/).
    - store the results in a db
    - calculate the contestants elo-rating
    - display a high-score-board

- Decided that the frontend will be built on `Bootstrap 5`and the backend will be built using `Django`

- Added script to scrape the pro-league url