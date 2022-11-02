## Prerequisites
    - Docker (at least 4.10.1)
## Running
```docker compose -f docker-compose.yml up --build```


## Folder Structure

## Testing

## REST API

## Logging, Alembic, Coverage, Black Autoformatter

## TODO
- Swagger docs
- this api needs better error handling
- discuss alternative ways to calculate the weather stats data
- this repo needs a makefile


docker compose -f docker-compose.yml up --build
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up 
docker exec -d corteva-weather_api-1 alembic init alembic
docker exec corteva-weather_api-1 alembic revision --autogenerate -m "Added tables"
docker exec corteva-weather_api-1 alembic upgrade head


docker exec corteva-weather_api-1 pylint models
docker exec corteva-weather_api-1 black .
docker exec corteva-weather_api-1 python3 ingest_data.py test.txt US_corn_grain_yield.txt

Pylint ignored rules C0114

