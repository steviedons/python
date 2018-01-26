# Input can be collected with input()
# age = input("How old are you? ")
# print("Are you really " + age + " years old!!!")

# if you want to convert this to an int then need to use int()

# The modulo operator is good for working out if something is odd or even
4 % 3 # is 1
5 % 3 # is 1
6 % 3 # is 0

# while loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Allowing the user to chose when to quit input

prompt = "Enter something and I will repeat it, use quit to exit: "
'''
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit': # This is to avoid the case where quit would be printed
        print(message)
'''

# Using a flag
'''
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''

# Using break to exit a loop
'''
prompt = "Please enter a city you have visited (use quit to finish):"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
'''
# Use continue in a loop if you want to skip the current iteration of the loop 

unconfirmed_users = ['steve', 'tracy', 'jack']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())

# If you want to removed all occurances of a word in a list

pets = ['cat', 'dog', 'fish', 'cat', 'dog']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a dict

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name: ")
    response = input("What hill should we climb tomorrow? ")

    responses[name] = response

    repeat = input("Would you like anyone else to take this poll? ")
    if repeat == 'no':
        polling_active = False

# Remember items returns the key and the value

for name, response in responses.items():
    print(name + " Would like to go for a ride up: " + response)
