from math import sqrt


def mudancaDeBase (n,base):
    conversao = []
    while n != 0:
        resto = n % base
        conversao.append(resto)
        n = int((n - resto)/base)
    return conversao


def modulo_n(a, n, k=1):
    expoentesBase2 = mudancaDeBase(k, 2)
    exp = a % n
    aPowExp_mod_n = 1
    for expoente in expoentesBase2:
        if expoente == 1:
            aPowExp_mod_n = (aPowExp_mod_n * exp) % n
        exp = (int(pow(exp, 2)) % n) % n
    return aPowExp_mod_n
a = 2
b = 3
c = 7
cifra = 121
print((cifra**k)%a)
