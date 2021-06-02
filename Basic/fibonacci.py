'''def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(6))
'''
num= int(input("Enter any number = "))
a= 0
b= 1
c= 0
ls= []
for i in range(num+1):
    ls.append(c)
    a= b
    b= c
    c= a+ b
print(ls)
print(f"{ls[num]} is at {num} position !")
