# Usage

1. Засетапить проект - `docker compose up -d`, `cd app && poetry install && python manage.py migrate`
2. `python manage.py runserver`
3. Открыть две вкладки терминала, в каждой быстро вставить следующее: `curl --location --request POST 'http://localhost:8000/api/v1/obtain/free' `

