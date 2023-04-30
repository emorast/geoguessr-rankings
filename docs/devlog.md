# geoguessr-elo Devlog
### 2023/03/30
- Solved a login problem. Instead of giving `requests.session().post()` the *payload* as an dict, a `.json`is given instead.
- Unfortunely called the API too many times. Looking into if it would be possible to pickle the session information (cookies etc.) and unpickle it instead of making another POST-request every tine the code runs.
- Started new `Django` project.

### 2023/04/29
- Working with the mockup for the application and figuring out what functionality would be implemented in the first version. To its core, the *geoguesr-elo* application have to be able to
    - scrape results from [GeoGuessr](https://www.geoguessr.com/).
    - store the results in a db
    - calculate the contestants elo-rating
    - display a high-score-board

- Decided that the frontend will be built on `React`and the backend will be built using `Django`.

- Added script to scrape the pro-league url.