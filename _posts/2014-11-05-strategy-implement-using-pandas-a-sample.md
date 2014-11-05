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

	data = pd.read_csv(r"")
	symbol = "6001991.SS."
	date_index = "Date"
	datetime_index = symbol + ".Datetime"	
	open_index = symbol + ".Open"
	close_index = symbol + ".Close"
	high_index = symbol + ".High"
	low_index = symbol + ".Low"
	volume_index = symbol + ".Volume"

	# Data cleaning and prepare
	df = data[data[volume]>0]
	def str2dt(format):
		def fstr2dt(str):
			return datetime.strptim(str, format)
		return fstr2dt
	df[datetime_index] = df[date_index].map(str2dt("%Y-%m-%d"))
	
	# add indicator which only needs series data
	donchian_max = lambda nparray: max(nparray)
	df["Donchian_upper"] = pd.rolling_apply(df[high_index], 55, donchian_max)

	# plot candlestick chart with volume
	# TODO: plot indicators
	# TODO: candlestick chart seems cost lots of resources, add options to plot close price chart only.	
	dt_num_index = symbol + ".DTN"
	df[DatetimeNum_index] = df[datetime_index].map(date2num)
	fig, (ax1, ax2) = plt.subplots(2, sharx=True)
	candlestick(ax1, df[[dt_num_index, open_index, close_index, high_index, low_index]].values)
	ax2.plot(df[dt_num_index], df[volume_index])
	plt.show()
	
