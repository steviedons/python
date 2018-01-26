import re

# Pass a raw string so you dont have to be escaped
# add the brackets to create groups within the regex and the ? means optional match
# with the ? this would match even if the number does not have an area code
phoneNumRegex = re.compile(r'(\d\d\d)?-\d\d\d-\d\d\d\d')
# Thia was .search in the example but that returns just one occurance if found
mo = phoneNumRegex.search('My number is 415-555-4242. And my second number 666-3232')
print('Phone number found: ' + (mo.groups())
