"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    set1 = str(list_one).strip('[]') + ','
    set2 = str(list_two).strip('[]') + ','
    if list_one == list_two:
        return EQUAL

    if set1 in set2:
        return SUBLIST
    
    if set2 in set1:
        return SUPERLIST

    return UNEQUAL