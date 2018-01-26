# Functions

# Basic greeting function

def greet_user(username):
    """Display a simple greeting"""
    print("Hello " + username.title())

greet_user("steve")

# positional arguments (order matters) and keyword arguments

def describe_pet(animal_type, pet_name):
    pass

# keywords are used when the function is called and can be in any order

describe_pet(pet_name='harry', animal_type='hamster')

