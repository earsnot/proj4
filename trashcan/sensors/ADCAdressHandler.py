# from constants import *
# import addresses from constant (LINE 1 & 10-12)

class ADCAddressHandler:
	"""docstring for """
	def __init__(self, address_selection_value):
		self.address_selection_value = address_selection_value

	def set_address(self, address):
		# address1 = import address1
		# address2 = import address2
		# address3 = import address3
		if self.address_selection_value == 0:
			return address1
		elif self.address_selection_value == 1:
			return address2
		elif self.address_selection_value == 2:
			return address3