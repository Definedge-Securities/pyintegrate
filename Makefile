install:
	poetry install

install_hooks:
	poetry run pre-commit install

install_poetry:
	curl -sSL https://install.python-poetry.org | python3 -

tests: install tests_only tests_pre_commit

tests_pre_commit:
	poetry run pre-commit run --all-files

tests_only:
	poetry run pytest -s tests/unit
