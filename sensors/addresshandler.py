# from constants import *
# import adresses from constant (LINE 1 & 10-12)

class ADCAdressHandler:
	"""docstring for """
	def __init__(self, adress_selection_value):
		self.adress_selection_value = adress_selection_value

	def set_adress(self):
		# adress1 = import adress1
		# adress2 = import adress2
		# adress3 = import adress3
		if self.adress_selection_value == 0:
			return adress1
		elif self.adress_selection_value == 1:
			return adress2
		elif self.adress_selection_value == 2:
			return adress3
