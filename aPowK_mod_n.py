from mudancaDeBase import mudancaDeBase
def modulo_n(a, n, k=1):
    expoentesBase2 = mudancaDeBase(k, 2)
    exp = a % n
    aPowExp_mod_n = 1
    for expoente in expoentesBase2:
        if expoente == 1:
            aPowExp_mod_n = (aPowExp_mod_n * exp) % n
        exp = (int(pow(exp, 2)) % n) % n
    return aPowExp_mod_n