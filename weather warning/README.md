
# Weather Warning

A Python Automation Program which sends a WhatsApp text to the user anytime the temperature crosses the user's threshold temperature. Using API reference and modules to get your latitude and longitude and the accurate temperature for that area. It warns you to keep you safe and avoid the hassle to check for the weather updates.

## Use

If you do not wish to check your temperature every hour when you go out or about to go out, you can use this code to allow you to get the weather for the city you are in. It reminds you to apply your sunscreen or find shade and avoid outdoors altogether!

## How it Works

You can fill a Google Form to input your phone number, city and threshold temperature. Using geopy module, the latitude and longitude values are accessed based on your city input.

The input values of the Google Form are accessed using Sheety API.

These values are fed into Open Weather API which returns the current temperature. If this temperature is greater than the threshold temperature then it will send you a WhatsApp warning text.

## APIs Used

* [Sheety API](https://sheety.co/)
* [Open Weather API](https://openweathermap.org/api)

## Demo

![WhatsApp Text by Twilio]()




