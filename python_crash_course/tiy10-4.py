"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

print("your name and I will add it to the guest list")
print("Enter 'q' to quit.")

with open("guest_book.txt", 'a') as file_object:

    while True:
        name = input('What is your name?: ')

        if name == 'q':
            break

        file_object.write(name + '\n')
        print ("Hello " + name.title() + " Your entry has been added to the guest -
        book")
