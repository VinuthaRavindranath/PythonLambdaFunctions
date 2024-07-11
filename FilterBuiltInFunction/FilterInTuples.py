# Filtering a List of Tuples with filter()
sales = [
    ('2022-06-01', 150),
    ('2022-06-02', 100),
    ('2022-06-03', 125),
    ('2022-06-04', 75),
    ('2022-06-05', 155),
    ('2022-06-06', 180)
]

filtered = list(filter(lambda x: x[1] >= 150, sales))
print(filtered)