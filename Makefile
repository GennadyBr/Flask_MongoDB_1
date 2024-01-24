upv:
	sudo docker-compose up -d --build

downv:
	sudo docker-compose down --remove-orphans

psv:
	sudo docker-compose ps

up:
	docker compose up -d --build

down:
	docker compose down --remove-orphans

ps:
	docker compose ps

net:
	sudo docker network create nginx_proxy

log:
	sudo docker logs flask_mongo_app
