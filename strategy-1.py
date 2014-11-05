from strategy import strategy

class patient(strategy):
	def __init__(self, instruments):
		strategy.__init__(self, instruments)
	
	def handle_data(self):
