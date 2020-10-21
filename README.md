# Архитектура высоконагруженных система. ДЗ №5
## L7-балансировка 1 лабы на двух виртуальных машинах в облаке


## Цель:
Необходимо:
> 1. Написать конфигурацию для L7-балансировщика (любого) для сервиса из ДЗ №1
> 1. Развернуть сервис из ДЗ №1 на двух виртуальных машинах в любом облаке
> 1. На отдельной виртуальной машине поднять балансировщик и настроить его на проксирование на сервис погоды из ДЗ №1



## Инструкция по установке:
1. Скачать/стянуть репозиторий
1. Перейти в папку репозитория
1. Выполнить команду `docker build -t <название образа> -f dockerfile . `, мною для работы используется исходный образ ubuntu, который дополнен наличием python'a. Поэтому для создания образов использую команды:
* `docker build -t ubuntu/archhightload_laba5_1 -f dockerfile1 .`
* `docker build -t ubuntu/archhightload_laba5_2 -f dockerfile2 .`
1. Выполнить команду `docker run -it --name <название контейнера> -p 127.0.0.1:<порт>:8000 ubuntu/archhightload_laba2` для создания docker-контейнера из docker-образа. В рамках задания были выполнены команды:
* `docker run -it --name laba5_1_archHL -p 127.0.0.1:5020:8000 ubuntu/archhightload_laba5_1`
* `docker run -it --name laba5_2_archHL -p 127.0.0.1:5030:8000 ubuntu/archhightload_laba5_2`











## Инструментарий:
- GIT (устанавливается командой `sudo apt install git -y`)
- Docker (устанавливается командой `sudo apt install -y docker-ce`) [дополнительная инструкция](https://losst.ru/ustanovka-docker-na-ubuntu-16-04)
- Nginx (устанавливается командой `sudo apt install nginx`) [дополнительная инструкция](https://losst.ru/ustanovka-nginx-ubuntu-16-04)
- GCC (устанавливается командой `sudo apt install build-essential`) [дополнительная инструкция](https://losst.ru/ustanovka-gcc-v-ubuntu-16-04)