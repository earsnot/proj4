#import init
import libs.constants
import pyboard as pyb

# EXPERIMENTAL
class ModeHandler:
    """Drive mode handler:
    """

    def __init__(self):
        self.mode = -1
        self.soc = -1

    def select_drivemode(self, mode=-1, soc=0):
        if mode == 0 or soc > 0 and soc <= 20:
            print('eco')
            eco.activate()
            normal.toggle()
            sport.toggle()

        elif mode == 1 or soc > 20:
            print('normal')
            eco.toggle()
            normal.activate()
            sport.toggle()

        elif mode == 2:
            print('sport')
            eco.toggle()
            normal.toggle()
            sport.activate()
        else:
            return(print("out of bounds"))



class Mode:
    def __init__(self, pin): #init constructor
        self.pin = pyb.Pin('pin', Pin.OUT_PP, pull=Pin.PULL_DOWN)
        self.is_active = False

    def activate(self):
        self.pin.value(1)
        self.is_active = True

    def deactivate(self):
        self.pin.value(0)
        self.is_active = False

    def toggle(self):
        if self.is_active:
            self.deactivate()




#mode = DriveModeHandler()
#mode.normal_mode()
#print(mode.normal_mode())

