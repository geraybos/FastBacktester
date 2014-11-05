import pandas as pd
import enum

class capital():
	def __init__(self, init_capital=None, symbols):
		if init_capital is None:
			self.init_capital = 100000
		self.free_margin = self.init_capital
		self.pnl = 0
		self.states = {}
		foreach symbol in symbols:
			self.states[symbol] = {'position':0, 'close_price':0, 'avg_price':0}
		self.orders = pd.dateframe(columns=['Datetime','Symbol','Quantity','Price','Commission','FreeMargin','PnL'])
		
	def new_trade(self, orders):
		foreach order in orders:
			datetime = order["Datetime"]
			symbol = order['Symbol']
			quantity = order['Quantity']
			price = order['Price']
			commission = order['Commission']
			self.free_margin -= commission
			if symbol.instrument_type == enum.InstrumentType.Stock:
				if quantity > 0:
					self.free_margin -= quantity*price*symbol.margin_ratio
					self.states[symbol][avg_price] = (self.states[symbol]['position']*self.states[symbol]['avg_price']+quantity*price)/(self.states[symbol]['position']+quantity)
					self.states[symbol]['position'] += quantity
				elif quantity < 0:
					if self.states[symbol]['position'] > -quantity:
						self.free_margin += -quantity*price*symbol.margin_ratio
						self.states[symbol]['avg_price'] = (self.states[symbol]['position']*self.states[symbol]['avg_price']+quantity*price)/(self.states[symbol]['position']+quantity)
						self.states[symbol]['position'] += quantity
					elif self.states[symbol]['position']+quantity == 0:
						self.free_margin += -quantity*price*symbol.margin_ratio
						self.states[symbol]['position'] = 0
						self.states[symbol]['avg_price'] = 0
					else:
						pass
						#TODO
					#TODO: margin check
			elif symbol.instrument_type == enum.InstrumentType.Future:
				self.free_margin -= abs(quantity*price*symbol.margin_ratio)
			self.orders[len(self.orders)+1] = [datetime, symbol, quantity, price, commission, self.free_margin, self.get_pnl(self)]
		
	def get_pnl(self):
		pnl = 0
		foreach key,val in self.positions:
			temp += val['position']*(val['close_price']-val['avg_price'])
		return temp
