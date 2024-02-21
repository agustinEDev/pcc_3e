import sys
sys.path.append('../clases/')
import clases.car as car

my_car = car.Car('audi', 'a4', 2009)
print(my_car.get_descriptive_name())
my_car.update_odometer(125000)
my_car.read_odometer()
my_car.update_odometer(124000)
my_car.increment_odometer(-13)
my_car.read_odometer()