# Theo Novak - September 2020
# AQI finder: Reports back air quality and weather information on given city.
# https://api-docs.iqair.com/?version=latest#detailed-response-example

import requests, json
from statesmap import abbrev_us_state
from weathermap import weathermap
from functions import windDirection, report, celcToFar, metersToMPH, degree_sign

# For testing purposes
# city = "Redding"
# state = "California"

# Using a hashtable of abbreviations to states, the user can type in their state as a
# two character abbreviation code.
city = input("Type a US city to check its air quality : ").title().strip()
state = input("What state is " + city + " in? : ").title().strip()
if(len(state) == 2):
	state = abbrev_us_state[state.upper()]

API_KEY = "d7b8f51b-10c1-4a82-9a48-8786e3b1948f"

url = "http://api.airvisual.com/v2/city?city=" + city + "&state=" + state + "&country=USA&key=" + str(API_KEY)
page = requests.get(url)

# dataDict has dataDict['status'], and dataDict['data']
dataDict = json.loads(str(page.text))

# Check acceptance of API request, then continue
if(dataDict.get('status') == 'success'):
	AQI = dataDict['data']['current']['pollution']['aqius']
	weather = dataDict['data']['current']['weather']
	# Reports the data on new lines, full report.
	# report(dataDict['data'])
	
	# Relevant report, reader-friendly
	print("\nWeather :: " + weathermap[weather['ic']])
	print("Temperature :: " + str(celcToFar(weather['tp'])) + degree_sign + "F")
	print("AQI :: " + str(AQI))
	print("Humidity :: " + str(weather['hu']) + "%")
	print("Wind :: " + str(metersToMPH(weather['ws'])) + " MPH " + str(windDirection(weather['wd'])))
else:
	print("\nSomething went wrong loading your results. Check your spelling and try again.")