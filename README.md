# Проект "CargoAPI"
Проект "CargoAPI" - это бэкенд-сайт для карго-сервиса kscargo.ru. В проекте администратор может добавлять отзывы и изображения о своем карго-сайте. Также в бэкенде реализована функциональность отправки SMS в Telegram админу, если у клиента возникают вопросы.

## Функциональности
1. Добавление отзывов и изображений администратором.
2. Отправка SMS в Telegram админу при появлении вопросов у клиентов.

## Технологии
1. Python
2. Django


## Установка и запуск

1. Клонировать репозиторий:

```
git clone https://github.com/idibek-alimov/cargoapi.git
```

2. Установить зависимости:

```
pip install -r requirements.txt
```

3. Применить миграции:

```
python manage.py migrate
```

4. Запустить сервер:

``` 
python manage.py runserver
```

После запуска сервера, API будет доступно по адресу http://localhost:8000.
