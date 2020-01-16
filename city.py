class City:
		def __init__(self, name, mayor):
				self.name = name
				self.mayor = mayor
				self.year_established = ''
				self.buildings = list()

		def add_buildings(self, buildings):
				self.buildings.extend(buildings)