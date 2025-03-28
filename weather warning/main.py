import os
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client
import requests
from geopy.geocoders import Nominatim
import datetime as dt

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# GET ALL THE API KEYS

API_KEY = os.getenv('API_KEY')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
SHEETY_ID = os.getenv('SHEETY_ID')
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_ID}/weatherWarnings/formResponses1'
SHEETY_USERNAME = os.getenv('sheety_username')
SHEETY_PASSWORD = os.getenv('sheety_password')

# API REQUEST TO GET THE GOOGLE SHEET THAT IS LINKED TO THE GOOGLE FORM

response = requests.get(url=SHEETY_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
result = response.json()

today = dt.datetime.today()

# ONLY RUN THE CODE DURING THE PEAK HOURS TO AVOID WASTING MY API CALLS

if 12 <= today.hour <= 16:

    for user in result['formResponses1']:
        try:
            number = user['whatsAppNumber\n(withCountryCode)'].strip()
        except AttributeError:
            number = f'+91{user['whatsAppNumber\n(withCountryCode)']}'
        city = user['city'].title()
        thresTemp = user['yourThresholdTempInCelsius']

        # GET THE LAT AND LNG VALUE FOR THE CITY SPECIFIED BY THE USER

        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(city)

        lat = location.latitude
        lng = location.longitude

        parameter = {
            'lat': lat,
            'lon': lng,
            'appid': API_KEY,
            'cnt': 4,
            'units': 'metric'
        }

        # GET THE TEMP FOR THE SPECIFIED LAT AND LNG

        response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameter)
        response.raise_for_status()

        data = response.json()
        temp = data['list'][0]['main']['temp']

        # ONLY IF THE TEMP IS GREATER THAN THE THRESHOLD TEMP THEN SEND A WARNING

        if temp > thresTemp:

            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=f'Temp in {city} is currently: {temp}°\nMake sure to avoid outdoors or wear sunscreen!',
                to=f'whatsapp:{number}'
            )
