# Working with Dictionaries in the Python map() Function
measurements = [
    {'length': 1.2, 'width': 2.1},
    {'length': 3.2, 'width': 3.5},
    {'length': 1.2, 'width': 1.5},
]

areas = list(map(lambda x: x['length'] * x['width'], measurements))
print(areas)