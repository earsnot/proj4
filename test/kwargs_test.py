class ModeHandler:
    def __init__(self):
        self.mode = -1
        self.soc = -1
        
    def select_drivemode(self, mode="default", soc="default"):
        self.mode = mode
        self.soc = soc
        if self.mode == 0 or self.soc <= 20:
            print("eco")
            print(self.soc)
            print(self.mode)
            #eco.activate()
            #normal.toggle()
            #sport.toggle()

        if self.mode == 1:
            print("normal")
            #eco.toggle()
            #normal.activate()
            #sport.toggle()

        if self.mode == 2:
            print("sport")
            #eco.toggle()
            #normal.toggle()
            #sport.activate()
handler = ModeHandler()
handler.select_drivemode(soc=19)
