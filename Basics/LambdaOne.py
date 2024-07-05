f1 = lambda num1,num2: num1 + num2
print(f1(2,3))

print("---------------------Default Values-----------------------------")

f2= lambda a, b=10 :a+b #b has default value as 10
print(f2(5))

print("----------------------Tuple Packing----------------------------")
'''
When creating a lambda expression, we can have a
parameter that will be assigned with a reference for a tuple
that holds the values that were passed over. 
'''
f3= lambda *numbers:len(numbers) 
print(f3(20,40,99,44,30,55))

print("-----------------------Dict Packing---------------------------")
'''
 When creating a lambda expression, we can have a
parameter that will be assigned with a reference for a dict
object that holds the values that were passed over together
with names of parameters. The keys will be the names of
the parameters. 
'''
f4 = lambda **data: data['width'] * data['height']
print(f4(width=4, height=5))






