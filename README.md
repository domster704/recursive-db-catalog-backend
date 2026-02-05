# AitiGuru test task

## Начало

Надо выполнить следующие команды по порядку:

1. Установить все зависимости

```bash
poetry install
```

2. Запустить контейнер PostgreSQL

```Bash
docker compose up -d --build
```

3. Запустить миграцию через Alembic

```bash
poetry run alembic upgrade head
```

4. Заполнить базу данных начальными данными.<br/>
   Это можно легко автоматизировать, перенеся функцию seed_initial_data в функцию lifespan в `container.py` , но я хотел
   показать, что умею создавать свои программы CLI через Typer

```Bash
poetry run seed-db
```