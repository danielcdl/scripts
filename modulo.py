from math import gcd, sqrt
from fatores import fatores


def modulo():

    while True:
        n = input("digite o numero: ")
        if n.isnumeric():
            n = int(n)
            if n > 1:
                break
            else:
                return

    j=0
    tentativa = []
    list_fatores = []
    for i in range(1,n):
        if i%100==0:
            print("|",end="")
        k = modulo_n(i,n,n-1)
        if k%i == 0:
            if n % i == 0:
                print()
                list_fatores.append(i)
                print("fatores = ", list_fatores)
                n = n / i
            j+=1
        #print("""n={}    a={}    a^(n-1) mod n = {}     mdc = {}    |   {}  {}  {}""".format(n,i,k,gcd(i,k),gcd(2,k),gcd(5,k),gcd(29,k)))
    print(j)
    print(sqrt(n))
    print(list_fatores)
    modulo()

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
modulo()