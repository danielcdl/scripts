
def fatores(n):
    fatores = []
    while n % 2 == 0 or 2 > n:
        n = divmod(n, 2)[0]
        fatores.append(2)
    i=3
    while i <=n:
        while n % i == 0:
            n = divmod(n,i)[0]
            fatores.append(i)
        i += 2
    return fatores
a = fatores(3271)
print(a)