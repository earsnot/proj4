import libs.constants
import pyboard as pyb

#LOWEST_THRESHOLD = 20    
#def SOC_based_mode_select(self, soc):
#    if soc < LOWEST_THRESHOLD: #compare SOC to const LOWEST_THRESHOLD
#        self.eco_mode()
#        print("is sustainable")
#    self.normal_mode()
#
# EXPERIMENTAL
class ModeHandler:
    def __init__(self):
        self.mode = -1
        self.soc = -1
    def select_drivemode(self, mode="default", soc="default"):
        if mode == 0 or soc <= 20:
            eco.activate()
            normal.toggle()
            sport.toggle()

        if mode == 1:
            eco.toggle()
            normal.activate()
            sport.toggle()

        if mode == 2:
            eco.toggle()
            normal.toggle()
            sport.activate()


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

