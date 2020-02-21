class Car():
	"""A simple attempt to represent a car"""
	def __init__(self,make, model, year):
		"""Initialize attibute to discribe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
#############################_Method_END_###############################
	def get_discriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + " " + self.make + ' ' + self.model
		return long_name.title()
#############################_Method_END_###############################
	def read_odometer(self):
		"""Print a statement showing th car's mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
#############################_Method_END_###############################
	def update_odometer(self,mileage):
		"""
		Set the odometer reading to the given value
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
#############################_Method_END_###############################
	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
##############################_CLASS_END_###############################
class Battery():
	"""A simple attempt to model a battery for an electic car."""	
	def __init__(self, battery_size = 70):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size
#############################_Method_END_###############################	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kw battery.")
#############################_Method_END_###############################
	def get_range(self):
		"""Print a statement about the range this battry provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size ==85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		"Upgraded the battery"
		if self.battery_size == 70:
			self.battery_size = 85
			
		
##############################_CLASS_END_###############################

class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	
	def __init__(self,make,model, year):
		"""
		Initialize attributes of  the parent class.
		Then intialize attributes specific to an electric car"""
		super().__init__(make,model,year)
		self.battery = Battery()
#############################_Method_END_###############################
	def fill_gas_tank(self):
		"""Electric catrs don't have gas tanks."""
		print("This car dosen't nee a gas tank!")
##############################_CLASS_END_###############################
my_tesla = ElectricCar("tesla","model s",2016)

print(my_tesla.get_discriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_volt = ElectricCar("chevrolet","volt", 2019)
print(my_volt.get_discriptive_name())
my_volt.battery.get_range()
my_volt.battery.upgrade_battery()
my_volt.battery.get_range()

