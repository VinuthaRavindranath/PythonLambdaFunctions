'''
To find cubes 
'''
items=[1,2,3,4,5]
def cube_of_number(item):
    return item**3
cubes=map(cube_of_number,items)
print(cubes)

print("----------------------------------------------------------------")

items=[1,2,3,4,5]
cubes=list(map(lambda x:x**3, items))
print(cubes)