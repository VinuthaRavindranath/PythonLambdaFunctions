'''
The Python reduce() function is part of the functools library, which provides opportunities for functional programming in Python.
Prior to Python 3, the function was a built-in function, but was moved into the standard library following the release of Python 3. 
The function takes a pre-defined function and applies it to every item in an iterable (such as a list or tuple) and returns a single, computed value.
'''

# Understanding the Process of the reduce() Function
from functools import reduce
myList=[1,2,3,4,5]
value = reduce(lambda a, b: a + b, myList)
print(value)