# Тестовое задание: *«Сервис уведомлений»*

## *Стек технологий*
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)


## *Kак запустить*

**Клонируем проект:**
```shell

```

**Создаем виртуальное окружение:**
```shell
python -m venv venv
```

**Активируем виртуальное окружение:**
```shell
source venv/Scripts/activate
```

**В файл .evn добавляем ваш токен:**
```TOKEN = '<token>'```

**Обновляем pip и устанавливаем зависимости:**
```shell
python -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

**Создаем и применяем миграции в базу данных:**
```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

**Запускаем сервер:**
```shell
python manage.py runserver
```

**Запускаем Celery:**
```shell
celery -A notification_service worker -l info
```

**Запускаем Flower:**
```shell
celery -A notification_service flower --port=5555
```

***

## *Установка проекта с помощью docker-compose*

**Клонируем проект:**
```

```

**В файл .evn добавляем ваш токен:**
```TOKEN = '<token>'```

**Запускаем контейнеры:**
```shell
docker-compose up -d
 ```

***

## *Развернутый проект можно посмотреть по ссылкам:*
### При запуске через Docker:

API проекта: **http://0.0.0.0:8000/api/** 

Клиенты: **http://0.0.0.0:8000/api/clients/** 

Сообщения: **http://0.0.0.0:8000/api/messages/** 

Рассылки: **http://0.0.0.0:8000/api/mailings/** 

Общая статистика по всем рассылкам: **http://0.0.0.0:8000/api/mailings/fullinfo/** 

Детальная статистика по конкретной рассылке: **http://0.0.0.0:8000/api/mailings/1/info/** 

Документация: **http://0.0.0.0:8000/docs/**

### При обычном запуске:

API проекта: **http://127.0.0.1:8000/api/** 

Клиенты: **http://127.0.0.1:8000/api/clients/** 

Сообщения: **http://127.0.0.1:8000/api/messages/** 

Рассылки: **http://127.0.0.1:8000/api/mailings/** 

Общая статистика по всем рассылкам: **http://127.0.0.1:8000/api/mailings/fullinfo/** 

Детальная статистика по конкретной рассылке: **http://127.0.0.1:8000/api/mailings/1/info/** 

Документация: **http://127.0.0.1:8000/docs/**

***

## Дополнительные задания, которые я выполнил:

<ol>
<li>Подготовил docker-compose для запуска всех сервисов проекта одной командой</li>
<li>Сделал так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в ней отображалось описание разработанного API.</li>
<li>Реализовал администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям.</li>
<li>Организовал обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки.</li>
<li>Реализовал дополнительную бизнес-логику: добавил в сущность "рассылка" поле "временной интервал", в котором можно задать промежуток времени и в котором клиентам можно отправлять сообщения с учётом их локального времени.</li>
</ol>
