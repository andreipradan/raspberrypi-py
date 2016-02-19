import time
import RPi.GPIO as GPIO


class Gpio:
    def __init__(self, outs=None, ins=None):
        outs = outs or []
        ins = ins or []
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        for o in outs:
            GPIO.setup(o, GPIO.OUT)
        for i in ins:
            GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def turn_on(self, led, verbose=False):
        GPIO.output(led, 1)
        if verbose:
            print('{}: on'.format(led))

    def turn_off(self, led, verbose=False):
        GPIO.output(led, 0)
        if verbose:
            print('{}: off'.format(led))

    def press(self, button, func=None, *args, **kwargs):
        input_state = GPIO.input(button)
        if input_state is False:
            if func:
                func(*args, **kwargs)
            else:
                print('Button {} Pressed'.format(button))
            time.sleep(0.2)

    def cleanup(self):
        GPIO.cleanup()
