import datetime

class Building:
		def __init__(self, address, stories):
				self.address = address
				self.stories = stories
				self.designer = ''
				self.date_constructed = ''
				self.owner = ''

		def __str__(self):
				return f"{self.owner}'s building at {self.address} is {self.stories} stories tall."

		def construct(self):
				self.date_constructed = datetime.datetime.now()

		def purchase(self, purchaser):
				self.owner = purchaser