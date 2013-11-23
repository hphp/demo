#!/usr/bin/python

class item:
    def __init__(self):
        self.name = ''
        self.size = 10
        self.list = []

class it:
    def __init__(self,s = 10):
		self.size = s
		self.name = ""
		self.list = []

class it_func:
	def __init__(self):
		self.size = 100
	def good(self):
		print "should use (self) as an argument"

def test_class_function():
	i = it_func()
	i.good()

test_class_function()

a = item()
a.name = 'cup'
a.size = 8
a.list.append('water')

b = it(2)
print b.size
