# Had to install xclip on a fedora gnome system for the clip baord part to work

import pyperclip
import re

# Phone number regex American numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|e|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# Email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Find the numbers and emails in the clipboard text

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails addresses found.')
