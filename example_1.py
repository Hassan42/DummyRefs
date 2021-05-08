from example import *
"""Move Method
obj = a + c and obj = a + func(c) are matched due to element sorting.
"""
class example_class_child(example_class):
	def methodC(self):
        print("Hello World")
    
	def methodB(self):
		obj = a + func(c)