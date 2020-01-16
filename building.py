import datetime

class Building:
		def __init__(self, address, stories):
				self.address = address
				self.stories = stories
				self.designer = ''
				self.date_constructed = ''
				self.owner = ''

		def construct(self):
				self.date_constructed = datetime.datetime.now()

		def purchase(self, purchaser):
				self.owner = purchaser