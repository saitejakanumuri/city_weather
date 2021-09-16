import requests
from prettyprinter import pprint

API_Key = 'c416f544f35b07231979188b6abfdeea'  #this API_KEY is copied from the openweathermap website.
city = input("Enter a city: ")
base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+API_Key+'&q='+city
weather_data = requests.get(base_url).json() #requests.get(URL/https request,parameters in {}].json()/.html()[required src] this return specific
pprint(weather_data) #pretty printer makes json text to dictionary key-value pairs