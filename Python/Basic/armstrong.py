num= input("Enter any number = ")

total=0
for i in num:
    temp= 1
    for j in range(len(num)):
        temp*= int(i)
    total+= temp

if total==int(num):
    print("armstrong")
else:
    print("Not A Armstrong")
