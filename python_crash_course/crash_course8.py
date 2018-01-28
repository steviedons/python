# Functions

# Basic greeting function

def greet_user(username):
    """Display a simple greeting"""
    print("Hello " + username.title())

greet_user("steve")

# positional arguments (order matters) and keyword arguments

#def describe_pet(animal_type, pet_name):
#    pass

# keywords are used when the function is called and can be in any order

# describe_pet(pet_name='harry', animal_type='hamster')

# Default value for parameters

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='bob')

'''
When you use default values, any parameter with a default value needs to be listed
after all the parameters that don’t have default values. This allows Python to con-
tinue interpreting positional arguments correctly.
'''
