'''
A pure function is a function that will return the same values given the same arguments. 
A function is not pure if there is something outside the function that can change its return,
given the same arguments. Below is an example of a pure function.
Given the same arguments, this function will always return the same output. 
It has no side effects. There is nothing outside the function that can change its return. 
For example, the argument that we have passed (12 and 45) will always return 12.0.

Reference :https://medium.com/@benjamin.BA/pure-functions-vs-impure-functions-in-python-b2f009664ee4
'''

def func(num1,num2):
    x=(num1*num2)/num2
    return x

print(func(12,45))

print("-------------------------------- writing the pure function using lambda function-----------------------------------------")

def convert(items,f):
    result=[]
    for item in items:
        result.append(f(item))
    return result

numbers1=[1,4,9]
numbers2 = convert(numbers1, lambda num: 10 * num)
print (numbers2)
