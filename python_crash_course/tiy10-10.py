'''
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
'''

def find_words(filename, find_word):
    """Given a filename and a word print out the number of occurances of the word in the file"""
    try:
        with open(filename) as file_object:
            first_line = file_object.readline()
            # Go back to the start of the file to include the title in the count
            file_object.seek(0)
            book = file_object.read()
            count = book.lower().count(word)
            print(first_line[1:].rstrip())
            print("The number of occurances of " + word + " is: " + str(count) + '\n')
    except:
        print("The " + filename + " file was not found\n")

word = input('What word do you want to search the list of books for? ')


books = ["1342-0.txt", "11-0.txt", '84-00.txt', '219-0.txt']

for book in books:
    find_words(book, word)