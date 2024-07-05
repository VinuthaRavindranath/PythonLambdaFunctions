'''
2. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# sorted_models = sorted(models, key=lambda x: x['model'])
sorted_models = sorted(models, key=lambda x: x['color'])

print(sorted_models)

print("------------------------------------------------------------------------------")

data = {7058: 'sravan', 
         7059: 'jyothika',
         7072: 'harsha', 
         7075: 'deepika'}

sorted_data =sorted(data.items(),key=lambda x:x[1])
print(sorted_data)

print("-------------------------------------------------------------------------------")

footballers_goals = {'Eusebio': 120,
                     'Cruyff': 104,
                     'Pele': 150,
                     'Ronaldo': 132,
                     'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)