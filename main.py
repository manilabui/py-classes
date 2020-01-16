# pizza
from pizza import Pizza

hawaiian = Pizza(16, 'thin')
hawaiian.add_topping('pineapple')
hawaiian.add_topping('ham')
hawaiian.output_order()

# urban planner
from building import Building

eight_hundred_eighth = Building("800 8th Street", 12)
print(eight_hundred_eighth.address)