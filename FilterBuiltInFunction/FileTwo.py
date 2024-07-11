# Filtering a List of Strings
# Filtering Words Longer than n Characters in a Python List
strings = ['hello', 'world', 'yes', 'no', 'maybe']

filtered = list(filter(lambda x: len(x) > 4, strings))
print(filtered)