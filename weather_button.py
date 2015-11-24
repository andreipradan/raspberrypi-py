import sys
import time
import requests
import RPi.GPIO as GPIO

from utils import Led
from settings import API_URL, API_KEY, CITY_IDS

button_in = 13
GPIO.setup(button_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)


led = Led()

params = '?id={}&appid={}&units=metric'.format(
    CITY_IDS['cluj_napoca'], API_KEY)


def request_data():
    print('requesting data from the weather API...')
    result = requests.get(API_URL + params)
    api_temp = result.json()['main']['temp']
    rounded_temp = int(round(int(api_temp)))
    print('temperature in cluj: {}'.format(rounded_temp))
    return rounded_temp


def light_temp(degrees):
    led.warm_up(leds=led.all)
    for i in range(degrees):
        led.flicker(leds=led.reds, frequency=0.2, times=1)
        led.flicker(leds=led.blues, frequency=0.2, times=1)
    time.sleep(0.5)

if len(sys.argv) > 1:
    if sys.argv[1] == 'get':
        light_temp(request_data())

try:
    print('Push the button to check temperature...')
    while True:
        input_state = GPIO.input(button_in)
        if input_state is False:
            light_temp(request_data())
except KeyboardInterrupt:
    print('Cleaning up GPIO...')
    GPIO.cleanup()
    print('Done!')
