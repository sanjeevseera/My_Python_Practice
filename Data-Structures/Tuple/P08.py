"""
Write a Python program to create the colon of a tuple
"""

from copy import deepcopy
#create a tuple
tuplex = ("HELLO", 5, [], True)
print(tuplex)
#make a copy of a tuple using deepcopy() function
tuplex_clone = deepcopy(tuplex)
tuplex_clone[2].append(50)
print(tuplex_clone)
print(tuplex)