def compound_intersest(p,t,r):
    A = p * (pow((1 + r / 100), t))
    CI = A - p
    print("Compound interest is", CI)
compound_intersest(20000, 12.13, 5)


