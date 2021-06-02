def total(num1, num2):          
    return num1+ num2
print(total(9, 19))

def total_2(*args):
    print(args)
    print(type(args))

total_2(1, 2, 3, 4, 5, 6, 7)

def total_3(*args):
    return sum(args)

print(total_3(1, 2, 3, 4, 5))