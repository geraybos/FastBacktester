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
			new_orders = self.handle_data(self, row, self.capital)
			if len(x)>0:
				self.capital.add_order(new_orders)
	def plot_total_pnl(self):
		pass
	def plot_symbol(self, symbol):
		symbol.plot_price()
	def handle_data(self, market_data, capital):
		pass
