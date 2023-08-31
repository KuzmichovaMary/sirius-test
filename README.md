# Что это за проект

Telegram Bot с finetuned ruDialoGPT.

[Ноутбук с дообучением](https://www.kaggle.com/marykuzmicheva/sirius-exam).

# Установка

! Скачайте файл [тык](https://huggingface.co/maryshca/fpmi-abitur-model/tree/main) в папку `server/model`

## Тестирование и локальный запуск

Необходим [питон версии 3.10>=](https://www.python.org/downloads/).

1. Установить `poetry`. ```curl -sSL https://install.python-poetry.org | python3 -
``` для Linux, MacOS и Windows WSL ```(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -``` для Windows PowerShell. (Не забудьте прописать путь до `poetry` в `PATH`)
2. Склонить проект ```git clone https://github.com/KuzmichovaMary/sirius-test.git```
2. Зайти в папку с сервером ```cd sirius-test/server```
5. Запустить ```poetry install --no-root```
6. Запустить ```poetry run python3 server.py```
2. Зайти в папку с ботом ```cd sirius-test/bot```
4. Создать файл `.env` с переменной `TG_BOT_TOKEN` или прописать эту переменную в переменные среды.
5. Запустить ```poetry install --no-root```
6. Запустить ```poetry run python3 bot.py```

## Запуск на сервере

Для работы необходим установленный докер ([как установить](https://docs.docker.com/engine/install/)) и [питон 3.10>=](https://www.python.org/downloads/).

1. Склонить проект ```git clone https://github.com/KuzmichovaMary/sirius-test.git```
2. Зайти в папку с сервером ```cd sirius-test/srever```
3. Собрать докер-образ ```docker build -t server .```
4. Запустить докер-образ ```docker run --name sirius-bot -it server -P``` посмотреть какой порт выделился.
5. Поменять `SERVER_URL` в файле `server.py`.
2. Зайти в папку с ботом ```cd sirius-test/bot```
3. Собрать докер-образ ```docker build -t bot --build-arg BOT_TOKEN=<YOUR TOKEN> .```
4. Запустить докер-образ ```docker run --name sirius-bot -it bot```
