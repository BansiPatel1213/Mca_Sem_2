def sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i * i

    return s
n = 2
print(sum(n))
