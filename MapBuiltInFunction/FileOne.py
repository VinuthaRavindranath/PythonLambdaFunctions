'''
You use the map() function whenever you want to modify every value in an iterable.

map(function, iterable)
'''

fruits=['apple','orange','banana','peach','kiwi']
length_list=[len(word)for word in fruits ]
print(length_list)

print("----------------------------------------------------------------")

fruits=['apple','orange','banana','peach','kiwi']
lengths=list(map(len,fruits))
print(lengths)

print("----------------------------------------------------------------")

fruits=['apple','orange','banana','peach','kiwi']
lengths=list(map(lambda x:len(x),fruits))
print(lengths)