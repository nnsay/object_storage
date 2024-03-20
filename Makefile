
active:
	poetry shell

lock: active
	poetry lock --no-update

install:
	poetry install

test: active
	poetry run pytest tests/

format: active
	poetry run ruff format .

varsion: active
	poetry run semantic-release version --no-commit --no-push --no-vcs-release
