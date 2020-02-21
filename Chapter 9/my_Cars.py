#importing a file through "module_name.class_name"
#import Car1

#The line below shows how to import multiple classes

from Car1 import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen","beetle",2016)
print(my_beetle.get_discriptive_name())

my_tesla = ElectricCar("tesla","model s",2016)
print(my_tesla.get_discriptive_name())
