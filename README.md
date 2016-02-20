# raspberrypi-py
The python library for controlling RaspberryPI components

### Installation
```
pip install raspberrypi-py
```

### Usage

* Using the Led object
  ```python
  from raspberrypi-py.components import Led
  
  led = Led(pins=[19, 13, 6, 12])   # initializing the Led class which will set up the gpio pins
  
  led.leds_on()                     # this will set the all the initialized leds on
  led.leds_on(leds=[19, 6])         # it is possible to turn on leds separately
  
  led.leds_off()                    # the same as above
  led.step_up(leds=[13, 12, 6])     # turns the leds on - one by one - in the specified order
  
  led.flicker(leds=[19, 6, 13, 13], frequency=0.05, times=10, ends_with='off') # flickers the leds (turns them on and off)
  
  led.pulse(leds=[6, 13], frequency=0.002, times=6)  # gives a pulsing feeling to the led using the wiringpi2 library
  ```

* Using the Button object
  ```python
  from raspberrypi-py.components import Button
  button = Button(pins=[13])    # instanciating the Button object with the pins that support output
  ```
  - simple check if the button is pressed
    ```python
    button.press(13)            # prints a message
    >>> "Button 13 is pressed"
    ```
  - creating custom actions that will trigger when the button is pressed
    + custom action that will be triggered:
    ```python
    def add_two(a, b):
        print(a+b)
    ```
    + actual code that checks and triggers the above action if pressed
    ```python
    try:
        print("Press the button to add 77 and 22")
        while True:
            button.press(13, add_two, 77, 22)
    except KeyboardInterrupt:
        print("Cleaning up GPIO...")
        button.gpio.cleanup()
    
    >>> 99
    ```

### Notes
Please read your RaspberryPI manual and/or any relevand documentation carefully before setting up your leds or buttons. Some pins are meant only for input(e.g. buttons) and some only for output(e.g. leds). 

Misusing your pins may inflict damage to your RaspberryPI.

Useful Raspberry PI B+ pinout diagram: https://www.raspberrypi.org/forums/viewtopic.php?f=78&t=82397
