build:
	docker compose build
run:
	docker compose up --detach
watch:
	docker compose up --watch
lint:
	uv run ruff check --fix
	uv run ruff format