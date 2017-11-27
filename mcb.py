# Usage: python mcb.py save <keyword> - Saves clipboard to keyword
#        python mcb.py <keyword> - Loads the keywork to clipboard
#        python mcb.py list - loads all keywords to clipboard
#        python mcb.py delete <keyword>
#        python mcb.py delete_all

import shelve
import pyperclip
import sys

# Save clipboard content
# with shelve.open('mcb') as mcbShelf:
#    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
#        print("Saving {0} to the shelf".format(pyperclip.paste()))
#        mcbShelf[sys.argv[2]] = pyperclip.paste()
#    elif len(sys.argv) == 2:
#        if sys.argv[1].lower() == 'list':
#            pyperclip.copy(str(list(mcbShelf.keys())))
#        elif sys.argv[1].lower() == 'delall':
#            print('Deleting all the contents of the shelf')
#            mcbShelf.clear()
#        elif sys.argv[1] in mcbShelf:
#            pyperclip.copy(mcbShelf[sys.argv[1]])
# Clearner way to do this:

with shelve.open('mcb') as mcbShelf:
    try:
        command = sys.argv[1].lower()

        if command == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif command == 'list':
            for key in mcbShelf.keys():
                print(key + "\n------------------")
                print(mcbShelf[key])
                print("\n------------------")
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif command == 'delete':
            del mcbShelf[sys.argv[2]]
        elif command == 'delete_all':
            mcbShelf.clear()
        else:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    except KeyError:
        print("That keyword does not exist")
