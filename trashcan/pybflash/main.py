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

mh = ModeHandler()
