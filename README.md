# corteva_challenge

docker compose -f docker-compose.yml up --build
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up
docker exec -d corteva-weather_api-1 alembic init alembic
docker exec -d corteva-weather_api-1 alembic revision --autogenerate -m "Added tables"
docker exec -d corteva-weather_api-1 alembic upgrade head