'''(a,b)=(2,0)
try:
    x=a/b
except ZeroDivisionError:
    print("Dividede Zero By Error")
    '''

#try-finally Caluse
x="Hello"
try:
   # x>3
    x=1/0
except NameError:
    print("You Have A Variable That Is Not Defined")
except TypeError:
    print("You Are A Compare Of Value Of Different Type")
except:
    print("Something else wrong")