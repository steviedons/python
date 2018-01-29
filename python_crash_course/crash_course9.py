class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age
        # setting a default value of an attribute
        self.legs = 4

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

    def get_name(self):
        """Return the dogs name"""
        return self.name

my_dog = Dog('Jet', '4')
print("My Dog's name is " + my_dog.name.title() + ".")
print("My Dog's name is " + my_dog.get_name().title() + ".")

my_dog.sit()
my_dog.roll_over()

print("\n\n\n")

from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# attributes within the class can be accessed directly with the dot notation
print("This car has " + str(my_new_car.odometer_reading) + " miles on it")

# updating through a value methong (update_odometer added to the class)

my_new_car.update_odometer(1000)
my_new_car.read_odometer()

# Class inheritance - the call inherits all the attributes and methods of the first class
# super() function links the child object to its parent


my_teslar = ElectricCar('tesla', 'model s', 2016)
print(my_teslar.get_descriptive_name())
print(my_teslar.describe_battery())

# Instances as attributes
'''
You’ll find that you have a
growing list of attributes and methods and that your files are becoming
lengthy. In these situations, you might recognize that part of one class can
be written as a separate class. You can break your large class into smaller
classes that work together.
For example, if we continue adding detail to the ElectricCar class, we
might notice that we’re adding many attributes and methods specific to
the car’s battery.
'''

# classes can be imported into other class module file

# The python standard library - example class is the OrderedDict from the module collection

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for first_name, language in favorite_languages.items():
    print(first_name.title() + "'s favorite language is " + language.title() + ".")
