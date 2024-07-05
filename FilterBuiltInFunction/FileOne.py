'''
Python’s filter() is a built-in function that allows you to process an iterable and 
extract those items that satisfy a given condition. This process is commonly known as a filtering operation. 
With filter(), you can apply a filtering function to an iterable and produce a new iterable with the items that satisfy the condition at hand. 
In Python, filter() is one of the tools you can use for functional programming.

https://realpython.com/python-filter-function/
'''

L=[3,6,7,9,12,14,19,21]

def even(x):
    if x%2 == 0:
        return True
    else:
        return False
    
f=filter(even,L)
for i in f:
    print(i)
    
print("------------------------------------------------------------filter() functions with lambda function ----------------------------------------------------------------")
    
L=[3,6,7,9,12,14,19,21]
    
f=filter(lambda num:num%2==0,L)
for i in f:
    print(i)

