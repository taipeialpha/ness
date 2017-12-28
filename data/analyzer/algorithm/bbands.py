#!/usr/bin/env python3

from math import pow, sqrt

mean = lambda array: sum(array)/len(array)
def std(array, xbar):
	s = float(0);
	for x in array:
		s += pow((x - xbar), 2)

	s /= (len(array) - 1)
	return sqrt(s)
	
class BollingerBands(list):
	def __init__(self, prices, length=20):
		list.__init__(self, prices)
		self.mean = mean(prices)
		self.std = std(prices, self.mean)
		self.length = length

	def append(self, price):
		if self.__len__() >= self.length:
			self.pop(0)
		list.append(self, price)
		self.mean = mean(self)
		self.std = std(self, self.mean)

	def value(self):
		return {'top': (self.mean + self.std*2),
			'middle': self.mean,
			'button': (self.mean - self.std*2)}

if __name__ == "__main__":
	bb = BollingerBands(list(range(20)))
	print(bb.value())
	bb.append(21)
	print(bb.value())
	print(len(bb))

# vim: ts=4 sw=4 noexpandtab
