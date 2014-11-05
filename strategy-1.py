from fast-backtester import instrument, capital_management

class strategy():
	def __init__(self, instruments, capital):
		self.instruments = instruments
		self.capital = capital
		self.df = pd.dataframe()
		foreach i in self.instruments:
			if self.df.empty:
				self.df = i.df
				self.datetime_index = i.datetime_index
			else:
				self.df = pd.merge(self.df, i.df, left_on=self.datetime_index, right_on=i.datetime_index)
	def run(self):
		
