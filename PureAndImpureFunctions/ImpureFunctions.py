'''
An impure function is ‘influenced’ by forces outside the function. 
With an impure function, given the same arguments, there is no guarantee that it will return 
the same output. The function below is not pure. 
This is because it is using a variable outside the function (global variable) — num3. 
If that variable changes, then given the same arguments, the return will also change. 
So, the function is not pure because it has side effects.

Reference : https://medium.com/@benjamin.BA/pure-functions-vs-impure-functions-in-python-b2f009664ee4
'''

num3=10
def func(num1,num2):
    x=(num1*num2)/num2*num3
    return x

print(func(12,45))

print("-------------------------------- writing the impure function using lambda function-----------------------------------------")
 
num2=10 # global variable, when changed the output will not be same
def convert(items,f):
    result=[]
    for item in items:
        result.append(f(item))
    return result

numbers1=[1,4,9]
numbers2 = convert(numbers1, lambda num: num2 * num)
print (numbers2)

