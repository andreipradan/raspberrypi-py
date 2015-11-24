from utils import Led

led = Led()

print('Start session')

while True:
    led.cycle(sleep=0.03)
