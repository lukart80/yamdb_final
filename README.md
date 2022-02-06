# yamdb_final
yamdb_final
https://github.com/lukart80/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg

# API_YamDB

REST API для сервиса YaMDb позволяет собирать обзоры пользователей на 
музыку, фильмы и сериалы. Также есть возможность оставлять комментарии к обзорам.


## Технологии
- python 3.8
- Django и Django Rest Framework
- база данных PostgreSQL
- веб сервер Nginx


## Запуск проекта с помощью Docker:
1  Клонируйте репозиторий `git clone https://github.com/lukart80/yamdb_final.git`

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

