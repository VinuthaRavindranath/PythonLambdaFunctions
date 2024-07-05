students=[
    ("mosh",123123,89),
    ("dan",435244,92),
    ("john",900953,82)
    ]

def f(std):
    return std[2]

student=max(students,key=f)
print(student)

'''
Max builtin function with key optional parameter
The key optional parameter allows us to specify the functionality
by which the items will be evaluated. 
'''
print("--------------------------------Max builtin function with lambda function as key optional parameter----------------------------------")

students=[
    ("mosh",123123,89),
    ("dan",435244,92),
    ("john",900953,82)
    ]


student=max(students,key=lambda x:x[2])
print(student)


products = [
    ('carpeta',990),
    ('tabola',200),
    ('chairex',880)
    ]

f =max(products, key=lambda product:product[1])
print(f)
