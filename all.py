import sys
import RPi.GPIO as GPIO

from utils import Led


def play(frequency=0.2):
    led = Led()

    print('Start session')

    while True:
        try:
            led.warm_up(leds=led.all, frequency=frequency)
            led.step_up(leds=led.all, frequency=frequency)
            led.flicker(leds=led.all, ends_with='on')
            led.step_down(leds=led.all[::-1], frequency=frequency)
            led.cycle(leds=led.all, frequency=frequency)
        except KeyboardInterrupt:
            print('Cleaning up...')
            GPIO.cleanup()
            print('Done.')

if __name__ == '__main__':
    try:
        frequency = float(sys.argv[1])
    except IndexError:
        frequency = None
    play(frequency)
