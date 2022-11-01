# corteva_challenge

docker compose -f docker-compose.yml up --build
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up 
docker exec -d corteva-weather_api-1 alembic init alembic
docker exec corteva-weather_api-1 alembic revision --autogenerate -m "Added tables"
docker exec corteva-weather_api-1 alembic upgrade head


docker exec corteva-weather_api-1 pylint models
docker exec corteva-weather_api-1 black .
docker exec corteva-weather_api-1 python3 ingest_data.py test.txt

Pylint ignored rules C0114