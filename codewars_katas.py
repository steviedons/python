# My code
'''
def elevator_distance(array):
    distance = 0
    for floor in range(0, len(array)-1):
        distance = distance + abs(array[floor] - array[floor+1])
    return distance
'''
# This code uses list comprehension

def elevator_distance(array):
    return sum(abs(array[i+1] - array[i]) for i in range(len(array)-1))

'''
When struggling to write a comprehension, don’t panic. Start with a for loop first and copy-paste your way into a comprehension.

Any for loop that looks like this:

new_things = []
for ITEM in old_things:
    if condition_based_on(ITEM):
        new_things.append("something with " + ITEM)

Can be rewritten into a list comprehension like this:

new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]

If you can nudge a for loop until it looks like the ones above, you can rewrite it as a list comprehension.
'''

'''
for letter in s:
    if letter in bad_control:
        bad = bad + 1
return str(bad) + '/' + str(len(s))
'''

# The above code worked but turned it into a comprehension

def printer_error(s):
    bad_control = 'nopqrstuvwxyz'
    
    bad_letters = [letter for letter in s if letter in bad_control]
    return str(len(bad_letters)) + '/' + str(len(s))

from re import sub

def printer_error_clever(s):
    # the sub removes any letters between a and m and then gets the length of what is left
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))