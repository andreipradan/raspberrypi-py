import sys

from raspberrypi_py.utils import Led


def play(times=None, frequency=None):
    led = Led()
    print('Start session')
    kwargs = {}
    if times:
        kwargs['times'] = times
    if frequency:
        kwargs['frequency'] = frequency
    led.pulse(**kwargs)

if __name__ == '__main__':
    try:
        times = int(sys.argv[1])
    except IndexError:
        times = None
    try:
        frequency = float(sys.argv[2])
    except IndexError:
        frequency = None
    play(times, frequency)
