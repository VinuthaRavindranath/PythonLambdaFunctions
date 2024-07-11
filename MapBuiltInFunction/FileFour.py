# Using String Methods with Python map()
quiet = ['hello', 'world', 'how', 'are', 'you']
yell = list(map(str.upper, quiet))

print(yell)

# Using String Methods with Arguments in Python map()
words = ['hello!', '!world', 'ho!w', 'ar!e', 'you!']
cleaned = list(map(lambda x: x.replace('!', ''), words))

print(cleaned)