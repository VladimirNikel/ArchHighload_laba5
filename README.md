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
1. На сервере/серверах:
  - Выполнить команду `docker build -t <название образа> -f dockerfile . `, мною для работы используется исходный образ ubuntu. Поэтому для создания образов использую команды:
    * `docker build -t ubuntu/archhightload_laba5_1 -f dockerfile1 .`
    * `docker build -t ubuntu/archhightload_laba5_2 -f dockerfile2 .`
  - выполнить команду `docker run -it --name <название контейнера> -p 0.0.0.0:<порт>:8000 ubuntu/archhightload_laba2` для создания docker-контейнера из docker-образа. В рамках задания были выполнены команды:
    * `docker run -it --name laba5_1_archHL -p 0.0.0.0:5020:8000 ubuntu/archhightload_laba5_1`
    * `docker run -it --name laba5_2_archHL -p 0.0.0.0:5030:8000 ubuntu/archhightload_laba5_2`
1. На третьем сервере необходимо установить Nginx (инструкция приложена) и прописать в конфигурационном файле `/etc/nginx/nginx.config` как в приложенном к репозиторию одноименном файле.
1. Потом выполнить команду перезапуска Nginx'а: `nginx -s reload`
1. Далее воспользуйтесь либо браузером по [адресу](http://127.0.0.1:80) `http://127.0.0.1:80/` либо воспользуйтесь терминалом:
  - `curl http://127.0.0.1:80/v1/current/?city=Moscow` - чтобы узнать текущую температуру в городе Moscow (можно использовать и другие города, хы)
  - `curl "http://127.0.0.1:80/v1/forecast/?city=Moscow&timestamp=3h"` - чтобы узнать прогноз погоды в интересующем Вас городе и используя *timestamp*:
    * `1h` - чтобы увидеть прогноз погоды на 1 час вперед
    * `3h` - чтобы увидеть прогноз погоды на 3 часа вперед
  	* `tomorrow` - чтобы увидеть прогноз погоды на завтра в это же время
  	* `yesterday` - чтобы увидеть какая погода была вчера в это же время



## Обновления:
* Добавлен в ответ сервера его ***"id_service"*** (по сути число 1 и 2, так как мы создали два сервера)
```python
my_id = sys.argv[1]

def current(city: str):
	...
	return json.dumps({"city": city,"unit": "celsius", "temperature": temp, "id_service": my_id})


def forecast(city: str, timestamp: str):
	...
	return json.dumps({"city": city,"unit": "celsius", "temperature": temp, "id_service": my_id})

```
* и в dockerfile тоже внесено изменение: передаем параметр - тот самый ***"id_service"***
```
python3 ./ArchHighload_laba5/main.py 1
```


## Инструментарий:
- GIT (устанавливается командой `sudo apt install git -y`)
- Docker (устанавливается командой `sudo apt install -y docker-ce`) [дополнительная инструкция](https://losst.ru/ustanovka-docker-na-ubuntu-16-04)
- Nginx (устанавливается командой `sudo apt install nginx`) [дополнительная инструкция](https://losst.ru/ustanovka-nginx-ubuntu-16-04)