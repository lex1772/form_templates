# Шаблон формы

Сервис для получения шаблонов форм по типам и названиям полей.

Пример шаблона формы:

{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}

Входные данные для веб-приложения:
Список полей со значениями в теле POST запроса.

Выходные данные:
Имя наиболее подходящей данному списку полей формы, при отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.


### Примеры запросов

1. POST `http://localhost:8000/` - получить форму
   
   Пример query parametrs:
   
   {}
  
   Пример ответа:

   "Нет данных"

   Пример query parametrs c не найденным шаблоном:
   
   {
   'my_date': 01-01-2000,
   'my_phone': %2B79998889988,
   'my_email': a@a.ru,
   'my_text': abc
   }
  
   Пример ответа:

   {
   'my_date': date,
   'my_phone': telephone,
   'my_email': email,
   'my_text': text
   }

   Пример query parametrs c найденным шаблоном:
   
   {
   'my_date': 01-01-2000,
   'my_phone': %2B79998889988,
   'my_email': a@a.ru,
   'my_text': abc
   }
  
   Пример ответа:

   {
   'name': My_template
   }

2. POST `http://localhost:8000/create` - создать шаблон формы

  Принимает JSON на вход и создает в базе новый шаблон
  
  {
   'name': 'Template'
   'my_date': '01-01-2000',
   'my_phone': '%2B79998889988',
   'my_email': 'a@a.ru',
   'my_text': 'abc'
   }

### Что сделано?

:white_check_mark: Реализовано REST API, принимающее на вход POST запросы.

:white_check_mark: Реализована фикстура для заполнения данными БД

:white_check_mark: Написаны тесты

:white_check_mark: База данных MongoDB запускается как Docker контейнер и настроен volume для сохранения данных.

:white_check_mark: Проект запускается через Docker-compose.


### Стек технологий:

- Django
- MongoDB
- Flake8
- python-dotenv
- Docker

### Начало работы с Docker-compose
1. Заполнить .env файл в соответствии с .env_sample
2. Создать образ с помощью команды `docker-compose build`
3. Запустить контейнеры с помощью команды `docker-compose up`
   
PS: Если фикстуры по какой-то причине не установились, то вручную через контейнер прописать `python manage.py loaddata template.json`

### Начало работы без Docker-compose
1. Заполнить .env файл в соответствии с .env_sample, но с указанием localhost в MongoDB вместо контейнера с БД
2. Наполнить базу данных командой `python manage.py loaddata template.json`
3. Запустить прложение командой `python manage.py runserver`
4. При желании запустить тесты командой `python manage.py test`

Приложение во всех случаях доступно по адресу `0.0.0.0:8000`
