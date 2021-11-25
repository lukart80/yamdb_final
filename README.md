# yamdb_final
yamdb_final
https://github.com/lukart80/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg

# API_YamDB
Проект доступен по адресу 51.250.21.112

REST API для сервиса YaMDb позволяет собирать обзоры пользователей на 
музыку, фильмы и сериалы. Также есть возможность оставлять комментарии к обзорам.


## Технологии
- python 3.8
- Django и Django Rest Framework

- база данных PostgreSQL
- веб сервер Nginx


## Запуск проекта с помощью Docker:
1  Создайте файл .env и укажите там следующие переменные окружения:
- EMAIL = 'yamdbapi@gmail.com'
- PASSWORD = 'm1n2b3v4'
- SECRET_KEY = 'p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs'
- ALLOWED_HOSTS = '*'
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=postgres
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=postgres
- DB_HOST=db
- DB_PORT=5432

2  Выполните комманду:
```
docker-compose up
```
3  Перейдите в терминал контейнера web приложения:

```
docker exec -it <CONTAINER_ID> bash
```
4  В контейнере выполните следующие команды:
```
python3 manage.py migrate

python3 manage.py createsuperuser
```
5  Для заполнения проекта данными выполните в терминале контейнера:
```
python3 manage.py loaddata fixtures.json
```
_________________________________

