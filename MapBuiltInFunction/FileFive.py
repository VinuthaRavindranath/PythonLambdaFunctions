'''
Write a Python program to create a dictionary that maps each character in the string input_string = "hello" to its corresponding ASCII value.
'''

input_string = "hello"

ascii_values=list(map(lambda x:ord(x),input_string))
print(ascii_values)

