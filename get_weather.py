import time
import requests
import RPi.GPIO as GPIO


from settings import API_URL, API_KEY, CITY_IDS
from utils import Led

params = '?id={}&appid={}&units=metric'.format(
    CITY_IDS['cluj_napoca'], API_KEY)

led = Led(verbose=True)


def request_data():
    print('Requesting data from the weather API...')
    result = requests.get(API_URL + params)
    api_temp = result.json()['main']['temp']
    rounded_temp = int(round(int(api_temp)))
    print('Temperature in Cluj-Napoca: {}\n'.format(rounded_temp))
    return rounded_temp


def light_temp(temp):
    led.warm_up(frequency=0.5)

    time.sleep(2)
    for i in range(temp):
        led.flicker(leds=led.all, frequency=0.3, times=1)
    time.sleep(0.5)

try:
    light_temp(request_data())
except KeyboardInterrupt:
    print('Cleaning up GPIO...')
    GPIO.cleanup()
    print('Done!')

