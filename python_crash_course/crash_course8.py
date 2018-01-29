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

# Return values - can be any data structure you want dicts / lists etc
'''
Modifying a List in a Function - pass by reference
When you pass a list to a function, the function can modify the list. Any
changes made to the list inside the function’s body are permanent, allowing
you to work efficiently even when you’re dealing with large amounts of data.
'''


def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    '''

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)
#print(unprinted_designs)

# To prevent this you can send a copy of the list to the function
# create a copy with the slice notation

# The function will still work the same as above but unprinted_designs will be the 
# same after the call
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# Passing an arbitary number of arguments - creates a tuple of the values passed

def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

make_pizza('ham')
make_pizza('ham', 'peppers', 'cheese')

'''
If you want a function to accept several different kinds of arguments, the
parameter that accepts an arbitrary number of arguments must be placed
last in the function definition.

def make_pizza(size, *toppings)
'''

'''
Using Arbitrary Keyword Arguments
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function.
'''

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('jack', 'donovan', location='godalming', age=8)

print(user_profile)

# Importing modules - created a pizza.py file with functions
# module_name.function()

import pizza

pizza.make_pizza(16, 'pepperoni')

# To import specific functions

from pizza import make_pizza

make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')

# using as to give a function an alias

from pizza import make_pizza as mp

mp(10, 'ham', 'cheese')

# using as to give a module an alias

import pizza as p

p.make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')

# importing all functions in a module - then every function can be called by name

from pizza import *

'''
However, it’s best not to use this approach when you’re working
with larger modules that you didn’t write: if the module has a function
name that matches an existing name in your project, you can get some
unexpected results.
'''

