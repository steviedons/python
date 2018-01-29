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

