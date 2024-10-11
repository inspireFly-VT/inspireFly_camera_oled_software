from time import sleep_us
from machine import Pin

"""
A class to represent a watchdog timer.

Attributes
----------
dog_pin : int
    The pin number used to control the watchdog.

Methods
-------
__init__(pin=20):
    Initializes the watchdog with the specified pin and sets it to off.

kick():
    Resets the watchdog timer by toggling the pin.

Example
-------
from watchdog import Watchdog
Dog = Watchdog(Pin(20, Pin.OUT))
Dog.kick()
"""

kick_time = 1
# default pin is 20
class Watchdog:
    def __init__(self, pin=20):
        self.dog_pin = pin
        self.dog_pin.off()

    def kick(self):
        # Pull high
        self.dog_pin.on()
        sleep_us(kick_time)
        # Pull low
        self.dog_pin.off()
