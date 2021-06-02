def even_or_odd( num):
    if num% 2== 1:
        return "Odd !"
    return "Even !"
num= int( input("Enter any number = "))
print( f"Your number is { even_or_odd( num)}")