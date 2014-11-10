import pandas as pd
import enum

class capital():
	def __init__(self, init_capital=None, instruments):
		if init_capital is None:
			self.init_capital = 100000
		self.free_margin = self.init_capital
		self.pnl = 0
		self.states = {}
		foreach instrument in instruments:
			self.states[instrument] = {'position':0, 'close_price':0, 'avg_price':0}
		self.orders = pd.dateframe(columns=['Datetime','instrument','Quantity','Price','Commission','FreeMargin','PnL'])
		
	def new_trade(self, orders):
		foreach order in orders:
			datetime = order["Datetime"]
			instrument = order['instrument']
			quantity = order['Quantity']
			price = order['Price']
			commission = order['Commission']
			self.free_margin -= commission
			if instrument.instrument_type == enum.InstrumentType.Stock:
				if quantity > 0:
					self.free_margin -= quantity*price*instrument.margin_ratio
					self.states[instrument]['avg_price'] = (self.states[instrument]['position']*self.states[instrument]['avg_price']+quantity*price)/(self.states[instrument]['position'] + quantity)
					self.states[instrument]['position'] += quantity
				elif quantity < 0:
					if self.states[instrument]['position'] > -quantity:
						self.free_margin += -quantity*price*instrument.margin_ratio
						self.states[instrument]['avg_price'] = (self.states[instrument]['position']*self.states[instrument]['avg_price']+quantity*price)/(self.states[instrument]['position']+quantity)
						self.states[instrument]['position'] += quantity
					elif self.states[instrument]['position'] + quantity == 0:
						self.free_margin += -quantity*price*instrument.margin_ratio
						self.states[instrument]['position'] = 0
						self.states[instrument]['avg_price'] = 0
					else:
						#TODO: Sell Short
						pass
					#TODO: margin check
			elif instrument.instrument_type == enum.InstrumentType.Future:
				self.free_margin -= abs(quantity*price*instrument.margin_ratio)
			self.orders[len(self.orders)+1] = [datetime, instrument, quantity, price, commission, self.free_margin, self.get_pnl(self)]
		
	def get_pnl(self):
		pnl = 0
		foreach key,val in self.states:
			temp += val['position']*(val['close_price']-val['avg_price'])*key.point_value
		return temp

	def get_instrument_trade(self, instrument):
		return self.orders[self.orders["instrument"] == instrument]
