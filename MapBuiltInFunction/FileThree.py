'''
multiply the value of list1 with the value of list2
'''

items=[1,2,3,4,5]
more_items=[10,20,30,40,50]

mapped=list(map(lambda x,y:x*y,items,more_items))
print(mapped)