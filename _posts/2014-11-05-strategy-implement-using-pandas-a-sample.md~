---
layout: post
title: "Strategy implement using pandas: a sample"
description: ""
category: 
tags: []
---
{% include JB/setup %}

	import pandas as pd
	from matplotlib.dates import date2num
	from matplotlib import pyplot as plt
	from matplotlib.finance import candlestick
	from datetime import datetime
	
	def str2dt(format):
		def fstr2dt(str):
			return datetime.strptim(str, format)
		return fstr2dt

	class instrument():
		def __init__(self, symbol, path, date_index=None, open_index=None,
					high_index=None, low_index=None, close_index=None,
					date_format=None):
			self.symbol = symbol
			self.path = path
			self.df = pd.read_csv(path)
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
			self.datetime_index = symbol + ".Datetime"	
			if date_format is None:
				self.date_format = "%Y-%m-%d"
			self.df[self.datetime_index] = df[self.date_index].map(str2dt("%Y-%m-%d"))
		def clean_data(self):
			df = data[data[volume]>0]
		def EWBBand(self, halflife):
			df[self.symbol+'.ewma'] = pd.ewma(df[self.close_index].shift(1), halflife)
			df[self.symbol+'.ewmstd'] = pd.ewmstd(df[self.close_index].shift(1), halflife)
			df[self.symbol+'.ewbb_upper'] = df[self.symbol+'.ewma'] + df[self.symbol+'.ewmstd']
			df[self.symbol+'.ewbb_lower'] = df[self.symbol+'.ewma'] - df[self.symbol+'.ewmstd']
		def Donchian(self, period):
			donchian_max = lambda nparray: max(nparray)
			donchian_min = lambda nparray: min(nparray)
			self.df[self.symbol+".Donchian_upper"] = pd.rolling_apply(self.df[self.high_index], period, donchian_max)
			self.df[self.symbol+".Donchian_lower"] = pd.rolling_apply(self.df[self.low_index], period, donchian_min)
		def plot_candle(self):
			self.dt_num_index = self.symbol + ".DTN"
			self.df[self.dt_num_index] = self.df[self.datetime_index].map(date2num)
			fig, (ax1, ax2) = plt.subplots(2, sharx=True)
			candlestick(ax1, self.df[[self.dt_num_index, self.open_index, self.close_index, self.high_index, self.low_index]].values)
			ax2.plot(self.df[self.dt_num_index], self.df[self.volume_index])
			plt.show()
		def plot_price(self):
			self.dt_num_index = self.symbol + ".DTN"
			self.df[self.dt_num_index] = self.df[self.datetime_index].map(date2num)
			fig, (ax1, ax2) = plt.subplots(2, sharx=True)
			ax1.plot(self.df[self.dt_num_index], self.df[self.close_index])
			ax2.plot(self.df[self.dt_num_index], self.df[self.volume_index])
			plt.show()
	
