class ModeSelector:
    drivemode = 0
    def get_drivemode(self):
        return self.drivemode

    def eco_mode(self):
        self.drivemode = 0
        return self.drivemode

    def normal_mode(self):
        self.drivemode = 1
        return self.drivemode

    def sport_mode(self):
        self.drivemode = 2
        return self.drivemode


# test

#mode = DriveModeHandler()
#mode.normal_mode()
#print(mode.normal_mode())

