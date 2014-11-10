import pandas as pd
from matplotlib.dates import date2num
from matplotlib import pyplot as plt
from matplotlib.finance import candlestick
from datetime import datetime
from enum import InstrumentType

def str2dt(format):
	def fstr2dt(str):
		return datetime.strptim(str, format)
	return fstr2dt

class instrument():
	def __init__(self, symbol, margin_ratio=None, instrument_type, point_value=None):
		'''Init an instrument, either stock or future. 
		For stock, the margin_ratio should be 1 for default.
		For Furture, you need to give margin_ratio and point_value.'''
		self.symbol = symbol
		if margin_ratio is None:
			self.margin_ratio = 1
		self.instrument_type = instrument_type
		if self.instrument_type == InstrumentType.Future:
			assert not point_value is None
			self.point_value = point_value
		else:
			self.point_value = 1
		self.df = pd.dataframe()

	def attach_historical_candles(self, path, date_index=None, open_index=None,
				high_index=None, low_index=None, close_index=None,
				date_format=None):
		'''Add historical candle data to instrument instance.'''
		self.path = path
		self.df = pd.concat(self.df, pd.read_csv(path))
		if date_index is None:
			self.date_index = "Date"		
		if open_index is None:
			self.open_index = symbol + ".Open"
		if close_index is None:
			self.close_index = symbol + ".Close"
		if high_index is None:
			self.high_index = symbol + ".High"
		if low_index is None:
			self.low_index = symbol + ".Low"
		if volume_index is None:
			self.volume_index = symbol + ".Volume"
		self.datetime_index = "DateTime"	
		if date_format is None:
			self.date_format = "%Y-%m-%d"
		self.df[self.datetime_index] = df[self.date_index].map(str2dt("%Y-%m-%d"))	
	def clean_data(self):
		'''Candle data cleaning.'''
		self.df = self.df[self.df[self.volume_index]>0]
	def get_daily_candle(self):
		'''Create daily candle data from existing dataframe'''
		self.daily_df = pd.dataframe()

	def ewbband(self, halflife):
		'''Create Expontenial Weighted Bollinger Band.'''
		self.df[self.symbol+'.ewma'] = pd.ewma(self.df[self.close_index].shift(1), halflife)
		self.df[self.symbol+'.ewmstd'] = pd.ewmstd(self.df[self.close_index].shift(1), halflife)
		self.df[self.symbol+'.ewbb_upper'] = self.df[self.symbol+'.ewma'] + self.df[self.symbol+'.ewmstd']
		self.df[self.symbol+'.ewbb_lower'] = self.df[self.symbol+'.ewma'] - self.df[self.symbol+'.ewmstd']
	def donchian(self, period):
		'''Create Donchian Channel.'''
		donchian_max = lambda nparray: max(nparray)
		donchian_min = lambda nparray: min(nparray)
		self.df[self.symbol+".donchian_upper"] = pd.rolling_apply(self.df[self.high_index], period, donchian_max)
		self.df[self.symbol+".donchian_lower"] = pd.rolling_apply(self.df[self.low_index], period, donchian_min)
	def std(self, period):
		'''Create Standard Dev.'''
		self.df[self.symbol.+".std"] = pd.rolling_std(self.df[

	def plot_candle(self, trades=None, **kwargs):
		self.__datetime2num(self)
		fig, (ax1, ax2) = plt.subplots(2, sharx=True)
		candlestick(ax1, self.df[[self.dt_num_index, self.open_index, self.close_index, self.high_index, self.low_index]].values)
		ax2.plot(self.df[self.dt_num_index], self.df[self.volume_index])
		self.__add_indicator_plot(self, ax1, ax2, kwargs)
		if not trades is None:
			self.__plot_trades(self, trades)
		plt.show()
	def plot_price(self, trades=None, **kwargs):
		self.__datetime2num(self)
		mondays = WeekdayLocator(MONDAY)
		mondays.MAXTICKS = 9999
		alldays = DayLocator()
		alldays.MAXTICKS = 9999
		weekDormatter = DateFormatter('%b %d')
		dayFormatter = DateFormatter('%d')
		fig, (ax1, ax2) = plt.subplots(2, sharx=True)
		ax1.plot(self.df[self.dt_num_index], self.df[self.close_index])
		ax2.plot(self.df[self.dt_num_index], self.df[self.volume_index])
		self.__add_indicator_plot(self, ax1, ax2, kwargs)
		if not trades is None:
			self.__plot_trades(self, ax1, trades)
		plt.show()
	def __plot_trades(self, ax, trades):
		buys = [(x["Datetime"], x["Price"] for x in trades if  x['Quantity']>0 ]
		buy_datetimes, buy_values = zip(*buys)
		ax.plot(buy_dates, buy_values, "^", markersize = 5, color = 'm')
		sells = [(x["Datetime"], x["Price"] for x in trades if  x['Quantity']<0 ]
		sell_datetimes, sell_values = zip(*sells)
		ax.plot(sell_dates, sell_values, "v", markersize = 5, color = 'k')
	def __add_pnl(self, pnl):
		pass
	def __datetime2num(self):
		self.dt_num_index = self.symbol + ".DTN"
		self.df[self.dt_num_index] = self.df[self.datetime_index].map(date2num)
	def __add_indicator_plot(self, ax1, ax2, **kwargs):
		for ax, indicator in kwargs:
			if ax == 1:
				ax1.plot(self.df[self.dt_num_index], self.df[self.symbol+"."+indicator])
			elif ax == 2:
				ax2.plot(self.df[self.dt_num_index], self.df[self.symbol+"."+indicator])
			else:
				
