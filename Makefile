SERVICE = web
COMPOSE = docker compose 


build:
	$(COMPOSE) build

up-build:
	$(COMPOSE) up --build

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d

enter:
	$(COMPOSE) exec $(SERVICE) bash

down:
	$(COMPOSE) down
