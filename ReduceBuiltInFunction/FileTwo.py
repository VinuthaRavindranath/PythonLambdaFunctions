'''
Write a Python program to find the longest word in the list words = ["apple", "banana", "cherry", "date"]using the reduce() function.
'''
from functools import reduce

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda a,b: a if len(a)>len(b) else b ,words)
print(longest_word)





# mylist=[]

# def length_of_word():
#     max_length = len(words[0])
#     for word in words:
#         if len(word)> max_length:
#             mylist.append(word)
#     return mylist
            
# print(length_of_word())

# longest_word = reduce(length_of_word, words)
