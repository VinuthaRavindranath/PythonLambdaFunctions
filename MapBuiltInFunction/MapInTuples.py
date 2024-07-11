# Using Python map() with Tuples
values = (1,2,3,4,5)
squares = tuple(map(lambda x: (x, x**2), values))

print(squares)