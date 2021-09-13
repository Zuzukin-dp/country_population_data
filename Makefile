SHELL := /bin/bash

manage_py := docker exec -it backend_ca

build:
	docker-compose down && docker-compose up -d --build

uvicorn:
	uvicorn main:app --host=0.0.0.0 --port=5000 --reload

migrations:
	$(manage_py) alembic init migrations

revision:
	$(manage_py) alembic revision --autogenerate -m "Added required tables"

upgrade:
	$(manage_py) alembic upgrade head

get_data:
	$(manage_py) python3 app/get_data.py

print_data:
	$(manage_py) python3 app/print_data.py
