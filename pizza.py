# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
class Pizza():
		def __init__(self, size, crust_type):
				self.size = size
				self.crust_type = crust_type
				self.toppings = list()

		def add_topping(self, topping):
				self.toppings.append(topping)

		def output_order(self):
				toppings_str = (' and ').join(self.toppings)
				print(f'I would like a {self.size}-inch {self.crust_type} pizza with {toppings_str}.')