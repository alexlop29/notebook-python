"""
What is a tuple?
An ordered, immutable list
"""

def reverseTuple(data: tuple) -> tuple:
    """
    Reverses a tuple

    Parameters:
    data: tuple

    Return:
    tuple
    """
    index = len(data) - 1
    reversed = ()

    while index >= 0:
        reversed = reversed + (data[index],)
        index -= 1
    
    return reversed

def simpleReverseTuple(data: tuple) -> tuple:
    """
    Reverses a tuple

    Parameters:
    data: tuple

    Return:
    tuple
    """
    return data[::-1]


tuple1 = (10, 20, 30, 40, 50)
print(reverseTuple(tuple1))
print(simpleReverseTuple(tuple1))

"""
Exercise 2: Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.
"""
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
first, second, third = tuple2
one, two, three = second
print(two)
# NOTE: (alopez) Leverages multi assignment unpacking
