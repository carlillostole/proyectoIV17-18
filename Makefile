install:
	pip install -r requirements.txt

test:
	cd TheWeatherBOT && python test_bd.py

execute:
	cd TheWeatherBOT && python bot.py
