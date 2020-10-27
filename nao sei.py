n = len(a)
ca = 1 / (dev_1 * math.sqrt(2 * math.pi))
cb = 1 / (dev_2 * math.sqrt(2 * math.pi))

# P({ai})
somai = 0
for i in range(1, n):
    somaj = 0
    for j in range(1, n):
        exponencial = math.exp(-0.5*(((a[i] - a[j]) / dev_1) ** 2 + ((b[i] - b[j]) / dev_2) ** 2))
        somaj = somaj + exponencial

    somai = somai + somaj

energia = ca * cb * somai / (n * n)