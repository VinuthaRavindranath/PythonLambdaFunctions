'''
Let's say we want to change 'g', 'b', 'e', 'b', 'g' to uppercase, and eliminate duplicate letters from the sequence. The following code performs this action:
'''

chars = {'g', 'b', 'e', 'b', 'g'}
upper_case=map(lambda x:x.upper(), chars)
print(set(upper_case))