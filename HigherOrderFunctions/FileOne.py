
def convert(items,f):
    result=[]
    for item in items:
        result.append(f(item))
    return result

def f(num):
    return 10*num

numbers1=[1,4,9]
numbers2=convert(numbers1,f)
print (numbers2)

print("-------------------------------- writing the above code using lambda function-----------------------------------------")

def convert(items,f):
    result=[]
    for item in items:
        result.append(f(item))
    return result

numbers1=[1,4,9]
numbers2 = convert(numbers1, lambda num: 10 * num)
print (numbers2)