'''
File to work on basic Python code
'''

message = "This is a test message"
print(message)

name = "ada lovelace"
print(name.center(20, "*").title())

print("Hello " + name.title() + "!")

# tabs and newlines
print("Languages:\n\tPython\n\tC\n\tJavascript")

# lstrip and rstrip - use this as well as lower() to get strings ready to store and compare
favourite_language = 'python '
print(favourite_language.rstrip())

# Or use strip to take away all whitespace
print(favourite_language.strip())

'''
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
'''

person = "jens Voigt"
quote = '"When my legs hurt, I say: “Shut up legs! Do what I tell you to do!""'

print(person.title() + " once said, " + quote)

# Avoid type errors with the str() / int() / float() functions
print(str(0.2 + 0.1))

print("3"*80)
##################################
# lists

'''
Because a list usually contains more than one element, it’s a good idea to make the
name of your list plural, such as letters , digits , or names .
'''

bicycles = ["Felt", "BMC", "Trek", "Cannondale",]
print(bicycles[-1])

bicycles[0] = "Canyon"
bicycles.append("Bianchi")
bicycles.insert(2, "Look")

print(bicycles)

del bicycles[1]
print(bicycles)

# pop can be used to remove items from the end of a list and then use it

popped_bike = bicycles.pop()
print(bicycles)
print(popped_bike)

# pop() can be used to pop any item in the list - to remove the first item
#first_bike = bicycles.pop(0)
#print(first_bike)

# remove() can be used to remove by value - get an error if the item is not in the list
#bicycles.remove("Trek")

# sort() can be used to sort a list
# reverse() can be used to reverse the order

#bicycles.sort(reverse=True)
#print(bicycles)

# To maintain the list as it was but sort it to display use sorted(list)
print("\n Here is the sorted list:\n" + str(sorted(bicycles)))

print("The list is of length: " + str(len(bicycles)))

print("4"*80)

##############################################
# running through a list with for

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick")

# Using range to generate a series of numbers
# the last value is off-by-one and is not included below ranges print out 9 as the last number

for value in range(1, 10, 2):
    print(value)

# can use range to create a list of values
numbers = list(range(1,10))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# functions that take a list of numbers min / max / sum
digits = list(range(1, 123, 3))
print(min(digits))
print(max(digits))
print(sum(digits))

######################################
# List Comprehensions

squares = [value**2 for value in range(1, 11)]
print(squares)

# [<expression> for <value> in <>]

# Looping through a slice
players = ['charles', 'jack', 'steve', 'tracy', 'bob']
print("Here are the first three players:")
for player in players[:3]:
    print(player.title())

print("Here are the last three players:")
for player in players[-3:]:
    print(player.title())

# to copy a list use a slice of the whole list
my_foods = ['pizza', 'choc', 'rice']
friend_foods = my_foods[:]

# if you just do friend_foods = my_foods then you are just creating a pointer to the same list
# updating one will update the other.

# tuples are immutable lists

dimensions = (200, 50)
# dimensions.append(20)
'''
Traceback (most recent call last):
  File "/home/steve/Dropbox/learning_python/python_crash_course/simple_message.py", line 136, in <module>
    dimensions.append(20)
AttributeError: 'tuple' object has no attribute 'append'
'''

print("5"*80)

################################
# for and if-elif-else

cars = ['audi', 'bMw', 'mazda']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'mazda' in cars:
    print("Mazda is in the list")


if 'vw' not in cars:
    print("VW is not in the list")

age = 66

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
# The else is not reguired but acts as a catch all at the end of the statement
else:
    price = 5

# The if-elif-else block will stop on the first true result
print("Your admission cost is $" + str(price) + ".")

'''
if you want only one block of code to run, use an if - elif -
else chain. If more than one block of code needs to run, use a series of
independent if statements.
'''

# Checking for a non empty list - an empty list evaluates to false

#requested_toppings = ["peppers"]
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza")

print("6"*80)

################################
# Dictionaries

'''
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
'''

alien_0 = {'color': 'green', 'points': 5}

print("Alien color: " + alien_0['color'])
print("Points for the alien: " + str(alien_0['points']))

alien_0['points'] = 10
print("Points for the alien are now: " + str(alien_0['points']))

'''
When you no longer need a piece of information that’s stored in a diction-
ary, you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to
remove.
'''

del alien_0['points']
print(alien_0)

# dict to store one kinf of information about objexct

favourite_languages = {
    'steve': 'python',
    'jack': 'kodu',
    'tracy': 'scratch',
    'bob': 'python',
    'jet': 'python',
}

# looping through a dict 

# each run of this could be different - the order of dicts is not kept
for key, value in favourite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

# if you just want the keys
for name in favourite_languages.keys():
    print("Name: " + name.title())

# This is the default behaviour so the below code is the same as above

for name in favourite_languages:
    print("Name: " + name.title())
    
print("\n")

# keys() returns a list of keys so you can then use in on it to fine a name

if 'daisy' not in favourite_languages.keys():
    print("Hey Daisy whats your favourite language?\n") 

# If you want the keys in a particular order then sort them before looping through them

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the survey.")

# values is the same but you use .values()

# if you want to get the values with no repetition you can use set(dict.values())

print("\nAll the languages mentioned in the poll:")
for language in set(favourite_languages.values()):
    print(language.title())

# Nesting dicts
'''
A more realistic example would involve more than three aliens with
code that automatically generates each alien. In the following example we
use range() to create a fleet of 30 aliens:
'''

# alien_0 = {'color': 'green', 'points': 5}

aliens = []

for alien in range(0, 30):
    aliens.append({'color': 'green', 'points': 5, 'speed': "slow"}) 

for alien in aliens[:5]:
    print(alien)

print("Number of aliens still alive: " + str(len(aliens)))

# A list in a dict

pizza = {
    'crust': 'thin',
    'toppings': ['chicken', 'peppers', 'chesse'],
}

print("You ordered a " + pizza['crust'] + " with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping.title())

# Example dict with multiple lists

favourite_languages = {
    'steve': ['python', 'c'],
    'jack': ['kodu', 'scratch', 'javascript'],
    'tracy': ['scratch'],
    'bob': ['python'],
    'jet': ['python'],
}

print("\n")

for name in favourite_languages:
    print(name.title() + "Favourite languages are: ")
    for language in favourite_languages[name]:
        print("\t" + language.title())

print("\n")
# The books answer was better and uses items() - although gets the same results:

for name, languages in favourite_languages.items():
    print(name.title() + "Favourite languages are: ")
    for language in languages:
        print("\t" + language.title())

# dict in a dict

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

'''
You should not nest lists and dictionaries too deeply. If you’re nesting items much
deeper than what you see in the preceding examples or you’re working with someone
else’s code with significant levels of nesting, most likely a simpler way to solve the
problem exists.
'''
