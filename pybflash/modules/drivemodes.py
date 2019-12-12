from libs.constants import *
from pyb import Pin

class Mode:
    def __init__(self, pin): #init constructor
        self.pin = Pin(pin, Pin.OUT_PP, pull=Pin.PULL_DOWN)
        self.is_active = False

    def activate(self):
        self.pin.value(1)
        self.is_active = True
        return self.is_active

    def deactivate(self):
        self.pin.value(0)
        self.is_active = False
        return self.is_active

#Has been tested and approved 08.12.19 by anders 'earsnot' rasmussen