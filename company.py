class Company:
		def __init__(self, name, industry):
				self.name = name
				self.address = ''
				self.industry = industry
				self.employees = list()

		def __str__(self):
				employee_names = ('\n * ').join([ employee.name for employee in self.employees ])
				return f'{self.name} is in the {self.industry} industry and has the following employees:\n * {employee_names}'

		def add_employees(self, employees):
				self.employees.extend(employees)