# Тестовое задание для компании "Техновизор"

## Описание выполненной задачи:

- Было разработано приложение для заказа корпоративной еды.
- Веб-приложение реализовано на фраймворке Django.
- Для верстки был использован bootstrap.


# Установка
## Клонируем репозиторий
    git clone git@github.com:Parcurcik/food-order-app.git

## Локальный запуск через виртуальное окружение

Необходимо в терминале прописать команды:

    python -m venv venv

    pip install -r requirements.txt
    
    python manage.py makemigrations
    python manage.py migrate

    python manage.py runserver

## Запуск через Docker

В файле settings.py изменить значение на:

    ALLOWED_HOSTS = ['0.0.0.0']

В корневой папке проекта прописать:

    docker-compose up

## Отчет по проделанной работе:

- Настроенный интерфейс Django-Admin, присутствуют фильтры
- Есть режим "Мне повезет" - случайным образом закидывает в блюда в заказ
- Формируется отчет по заказам на выбранную дату
- [Приложение лежит на хостинге](http://placerememberbezborodov.pythonanywhere.com/)
