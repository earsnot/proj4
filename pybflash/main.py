from modules.init import *

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
            normal.deactivate()
            sport.deactivate()
            self.mode = 0

        elif mode == 2 and soc > 20:
            print('sport')
            eco.deactivate()
            normal.deactivate()
            sport.activate()
            self.mode = 2

        elif mode == 1 or soc > 20:
            print('normal')
            eco.deactivate()
            normal.activate()
            sport.deactivate()
            self.mode = 1


        else:
            return(print("out of bounds"))

mh = ModeHandler()
