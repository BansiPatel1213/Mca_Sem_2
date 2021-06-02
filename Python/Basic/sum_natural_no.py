def squaresum(n):

    a = 0
    for i in range(1, n + 1):
        a = a + (i * i)

    return a
n = 12
print(squaresum(n))
