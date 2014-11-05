from fast-backtester import instrument, capital_management

class strategy():
	def __init__(self, instruments, capital=None):
		self.instruments = instruments
		if capital is None:
			self.capital = new capital(instruments)
		else:
			self.capital = capital
		self.df = pd.dataframe()
		foreach i in self.instruments:
			if self.df.empty:
				self.df = i.df
				self.datetime_index = i.datetime_index
			else:
				self.df = pd.merge(self.df, i.df, left_on=self.datetime_index, right_on=i.datetime_index)
	def run(self):
		foreach row in self.df:
			self.capital.new_order(self.handle_data(self, row))
	def plot_total_pnl(self):
		pass
	def plot_symbol(self, symbol):
		pass
	def handle_data(self):
		pass
