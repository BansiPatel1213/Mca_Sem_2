def calc_fact(x):
    if x == 1:
     return 1
    else:
     return(x*calc_fact(x-1))
n=5
print("1*2*3*4*5=",calc_fact(n))



