# Filtering a List of Dictionaries with the Python filter() Function
ages = [
    {'name': 'Evan', 'age': 25},
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 27},
    {'name': 'Jack', 'age': 32},
]

filtered = list(filter(lambda x: x['age'] >= 30, ages))
print(filtered)