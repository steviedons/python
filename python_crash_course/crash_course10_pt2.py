# Storing data - using the json module

import json
numbers = list(range(0, 20, 2))

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


# filename = 'username.json'

# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We will remember you when you return")
# else:
#     print("Welcome back, " + username)

# Refactoring


def get_stored_username():
    """Get the stored user name if it's available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
