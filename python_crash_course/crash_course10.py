# Chapter 10 Files and exceptions

# Opening a file and reading all the contents at once

# Note: when running this in the VSC terminal must be in the same directory as the text file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n\n')

# Reading the file contents line by line with absolute path

filename = '/home/steve/python/python_crash_course/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        # rstrip used to remove the newline character read in from the file otherwise you get double
        print(line.rstrip())

# Access to the file is only available inside the with block so assign the lines to a list

print('\n\n')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

'''
When Python reads from a text file, it interprets all text in the file as a string. If you
read in a number and want to work with that value in a numerical context, you’ll
have to convert it to an integer using the int() function or convert it to a float using
the float() function.
'''

# Writing to an empty file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming\n")

# Files are opened in 'r' read, 'w' write, append mode ('a') or 'r+' which is read / write mode

# Exceptions

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter numbers only")   
    else:
        print(answer)   

'''
Failing Silently - To do this in the except: clause add pass which will do nothing

The pass statement also acts as a placeholder. It’s a reminder that you’re
choosing to do nothing at a specific point in your program’s execution
and that you might want to do something there later.
'''

# Storing data

