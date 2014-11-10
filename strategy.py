from fast-backtester import instrument, capital_management

class strategy():
	self.instruments = []
	def __init__(self, instruments, capital=None):
		self.instruments = instruments
		if capital is None:
			self.capital = capital(instruments)
		else:
			self.capital = capital
		self.df = pd.dataframe()
		self.datetime_index = "DateTime"
		foreach i in self.instruments:
			if self.df.empty:
				self.df = i.df
			else:
				self.df = pd.merge(self.df, i.df, on=self.datetime_index)

	def run(self):
		for row_num in range(0, len(self.df)):
			new_orders = self.calculate(self, row_num, self.df, self.capital)
			if len(new_orders)>0:
				self.capital.add_orders(new_orders)

	def plot_total_pnl(self):
		pass
	def plot_symbol(self, instrument):
		symbol.plot_price()
	def handle_data(self, market_data, capital):
		pass
