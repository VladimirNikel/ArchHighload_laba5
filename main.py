from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

import uvicorn

#необходимо, чтобы работать с json'ом
import json

#необходимо для работы с переменными окружения
import os
import sys

#необходимо для работы с API openweathermap
import pyowm
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

config_dict = get_default_config()
config_dict['language'] = 'ru'

#тут находится ключ с сайта OpenWeatherMap
app_key = os.environ.get('OWM_APP_KEY')
owm = pyowm.OWM(app_key, config_dict)

my_id = sys.argv[1]

@app.get("/")
def print_web():
	html_content = """
		<html>
	<head>
	<title>Погодный сервис</title>
	<style>
		button.knopka {
		color: #fff; 
		background: #FFA500; 
		padding: 5px; 
		border-radius: 5px;
		border: 2px solid #FF8247;
		} 
		button.knopka:hover { 
		background: #FF6347; 
		}
	</style>
	</head>
	<body>
		<h1>Погодный сервис от Nikel</h1>
		<table>
		<tr>
			<td>
				<p>Узнать текущую погоду</p>
				<form action="/v1/current/" method="GET" name="form1">
					<input name="city" type="text" />
					<button class="knopka">Перейти сюда</button>
				</form>
			</td>
		</tr>
		<tr>
			<td>
				<p>Узнать прогноз погоды</p>
				<form action="/v1/forecast/" method="GET" name="form2">
					<input name="city" type="text" />
					<select name="timestamp">
						<option>Выберите из списка</option>
						<option>1h</option>
						<option>3h</option>
						<option>tomorrow</option>
						<option>yesterday</option>
					</select>
					<button class="knopka">Перейти сюда</button>
				</form>
			</td>
		</tr>
		</table>
	</body>
	</html>
	"""
	return HTMLResponse(content=html_content, status_code=200)

@app.get("/v1/current/")
#city=<name city>
#http://127.0.0.1:8000/v1/current/?city=Moscow
def current(city: str):
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(city)
	w = observation.weather
	temp = w.temperature('celsius')['temp']
	#вывод в консоль
	print(" request: " + city + "\t" + w.detailed_status + "\t" + str( temp ))
	return json.dumps({"city": city,"unit": "celsius", "temperature": temp, "id_service": my_id})


@app.get("/v1/forecast/")
#city=<name city>&timestamp=<timestamp>
#http://127.0.0.1:8000/v1/forecast/?city=Moscow&timestamp=3h
def forecast(city: str, timestamp: str):
	mgr = owm.weather_manager()

	observation = mgr.forecast_at_place(city, "3h") #данной командой стягивается прогноз погоды на ближайшие 5 дней с частотой 3 часа
	if timestamp == "1h":
		time = timestamps.next_hour()
	elif timestamp == "3h":
		time = timestamps.next_three_hours() 
	elif timestamp == "tomorrow":
		time = timestamps.tomorrow()
	elif timestamp == "yesterday":
		time = timestamps.yesterday()
	else:
		time = timestamps.now();
	w = observation.get_weather_at(time)
	temp = w.temperature('celsius')['temp']
	#вывод в консоль
	print(" request: " + city + "\ttime: "+ str(time) + "\t" + w.detailed_status + "\t" + str( temp ))
	return json.dumps({"city": city,"unit": "celsius", "temperature": temp, "id_service": my_id})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)