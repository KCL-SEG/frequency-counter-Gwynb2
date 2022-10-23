"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if type(item) == int:
            s =str(item)
            if s in frequencies:
                frequencies[s] += 1
            else:
                frequencies[s] = 1
        else:
            if item in frequencies:
                frequencies[item] += 1
            else:
                frequencies[item] = 1
    # Your code goes here
    return frequencies
list  = ["yes","yes","no",1,2,2,2]
