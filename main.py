# pizza
from pizza import Pizza

hawaiian = Pizza(16, 'thin')
hawaiian.add_topping('pineapple')
hawaiian.add_topping('ham')
hawaiian.output_order()

# urban planner
from building import Building

building_1 = Building("800 8th Street", 12)
building_2 = Building("300 5th Street", 10)
building_3 = Building("10 21st Street", 52)
building_4 = Building("109 9th Street", 34)
building_5 = Building("1900 2nd Street", 20)
building_1.purchase('Manila')
building_2.purchase('Manila')
building_3.purchase('Manila')
building_4.purchase('Manila')
building_5.purchase('Manila')

# employees
from employee import Employee
from company import Company

employee_1 = Employee('Michael Chang')
employee_2 = Employee('Martina Navritilova')
employee_3 = Employee('Serena Williams')
employee_4 = Employee('Roger Federer')
employee_5 = Employee('Pete Sampras')
company_1 = Company('Acme Explosives', 'chemical')
company_2 = Company('Jetways', 'transportation')

company_1.add_employees([employee_1, employee_2])
company_2.add_employees([employee_3, employee_4, employee_5])

print(company_1)
print(company_2)

# urban planner 2
from city import City

megalopolis = City('Manila', 'me')
megalopolis.add_buildings([building_1, building_2, building_3, building_4, building_5])

for building in megalopolis.buildings:
    print(building)