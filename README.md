## Prerequisites
    - Docker (at least 4.10.1)
Built using flask, alembic, SQLalchemy
## Running
1. Start the Server: ```docker compose -p challenge -f docker-compose.yml up --build```
2. Ingest Data (should take just a few seconds): ```docker exec challenge-weather_api-1 python3 ingest_data.py```

## REST API
At this point, you can browse the various endpoints using query strings. Below are 3 example queries you can run (tested with Postman):

Get all weather data for one day and station:
```http://127.0.0.1:5000/api/weather?date=19850103&station=USC00110072&page=1&per_page=5```

Get yield data for one year:
```http://127.0.0.1:5000/api/yield?year=2000&page=1&per_page=5```

Get weather stats for one year and station:
```http://127.0.0.1:5000/api/weather/stats?year=1985&station=USC00110072&page=1&per_page=5```
## Folder Structure
**I could've done this with a minimum number of folders and files. Why did I take this approach?**
The simple answer is that this API is designed to be scalable. Requirements grow over time, this API
is designed to grow as much as it needs to with minimal refactoring.

- **Config:** General Flask configuration
- **Controllers:** The functions that the API use live here.
- **Dockerfiles:** Location for all dockerfiles. Right there is only one, but as more environments are added, the project can handle it.
- **Helpers:** Location for all helper methods that are not official API controllers. Constants live here, as well as decorators.
- **Instance:** SQLITE instance location.
- **Logs:** Location for ingestion and API logs.
- **Models:** Where the data models live. They are separated into files to make it easier to find.
- **Tests:** Tests for python code, it mirrors top-level folder structure to make it easier to find tests.
- **Views:** Where The API views/endpoints live.
## Code Details
- The repo needs the ingest script in `ingest_data.py` to work appropriately.
- The ingestion script uses `multiprocessing` but SQLITE limits how many transactions can run.
- The timing data should be in the logs.
- The database rejects duplicates because of primary keys.
- `Pandas` is used to deal null values and reading/writing table data.
- **Where are the comments on every function/method?** I didn't get around to adding them, they would be helpful for Swagger. Otherwise, the code uses descriptive function and variable names that should help with reading what each function does.
## Testing
Testing was done via `unittest`, only two controllers have tests. Mocks were used in the process. Sorry I would do more testing if I had more time!


## Logging, Alembic, Coverage, Black Autoformatter, Pylint
- Logging was done via the `logging` library, two logs output to the logs folder. One for the ingestion process, one for the API.
- Alembic was integrated as the migration management system, feel free to browse the migration scripts in the `alembic` folder.
- the black autoformatter was integrated and ran on all files.
- Some files were linted via pylint. Pylint ignored rule C0114
## Code Details

## TODO
- Swagger docs
- this api needs better error handling
- discuss alternative ways to calculate the weather stats data
- this repo needs a makefile

