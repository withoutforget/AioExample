build:
	docker compose build
run:
	docker compose up --detach
down:
	docker compose down
stop:
	docker compose stop
watch:
	docker compose up --watch
lint:
	uv run ruff check --fix
	uv run ruff format