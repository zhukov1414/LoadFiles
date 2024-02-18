# Цель: Загрузка и обработка файлов

## Описание проекта:
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

## Возможности проета:
1.Создать Django проект и приложение.

2.Использовать Django REST Framework для создания API.

3.Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:
file: поле типа FileField, используемое для загрузки файла.
uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
processed: поле типа BooleanField, указывающее, был ли файл обработан.

4.Реализовать сериализатор для модели File.

5.Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.

6.Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.

7.Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.

## Как запустить локально:

1. Клонировать репозиторий и перейти в него:
3. Запустить docker-compose.yml, выполнить миграции

```bash
docker compose up
docker compose exec backend python manage.py migrate
```


## Cсылка на swagger:
Тестирование с файлами проводить через postman
https://localhost:8000/swagger
