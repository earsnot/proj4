LOWEST_THRESHOLD = 20

class ModeSelector:
    drivemode = 0 #initializing drivemode variable

    def get_drivemode(self): #method to return current drivemode
        return self.drivemode

    def eco_mode(self):
        #set_pin(129) #set controlsignal pin
        self.drivemode = 0 
        return self.drivemode #return current drivemode

    def normal_mode(self):
        #set_pin #set control signal pin
        self.drivemode = 1
        return self.drivemode  #return current drivemode

    def sport_mode(self):
        #set_pin #set control signal pin
        self.drivemode = 2
        return self.drivemode #return current drivemode

    def SOC_based_mode_select(self, soc):
        if soc < LOWEST_THRESHOLD: #compare SOC to const LOWEST_THRESHOLD
            self.eco_mode()
            print("is sustainable")

    


# test

ms = ModeSelector()
ms.SOC_based_mode_select(15)


#mode = DriveModeHandler()
#mode.normal_mode()
#print(mode.normal_mode())

