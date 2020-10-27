def mdc(numeros: list):
    numeros = list(set(numeros) - {0})
    if len(numeros) > 0:
        mdc = valor_absoluto(numeros[0])
        for numero in numeros[1:]:
            if mdc > valor_absoluto(numero):
                a = mdc
                b = valor_absoluto(numero)
            else:
                a = valor_absoluto(numero)
                b = mdc

            while b != 0:
                resto = a % b
                a = b
                b = resto
            mdc = a
        return mdc
    else:
        raise ValueError


def simplificar_fracao(numerador: int, denominador: int):
    divisor = mdc([numerador, denominador])
    numerador /= divisor
    denominador /= divisor
    return int(numerador), int(denominador)


def fracao(numero: float, dizima: bool = False):
    if dizima:
        pass
    else:
        digitos = len(str(numero).split('.')[1])
        denominador = int(calc_potencia(10, digitos))
        numerador = numero * denominador

    return simplificar_fracao(numerador, denominador)


def calc_potencia(base: float, expoente: float):
    a = base

    if expoente == 0:
        if a == 0:
            raise ValueError
        else:
            return 1
    else:

        if int(expoente) == expoente:
            n = expoente
            potencia = a
            for i in range(2,n+1):
                potencia *= potencia
        else:
            m, n = fracao(expoente)
            potencia = calc_raiz(calc_potencia(a,n), m)
        return potencia

def calc_raiz():
    pass

def raiz_quadrada(x):
    E = 0.000000001
    r_0 = x
    r_1 = (1 / 2 * (r_0 + (x / r_0)))
    erro = erro_relativo(r_1, r_0)
    while erro > E:
        r_2 = (1 / 2 * (r_1 + (x / r_1)))
        erro = erro_relativo(r_2, r_1)
        r_1 = r_2
    return x


def valor_absoluto(x):
    if x < 0:
        x = x * (-1)
    return x


def erro_relativo(x, y):
    if y == 0:
        x = 1
    else:
        x = (x - y) / y

    return valor_absoluto(x)


def somatorio(j, k):
    S = 0
    if j > 0:
        S = (1 - calc_potencia((1 / (1 + j)), k)) / (1 - (1 / (1 + j)))
    elif j == 0:
        S = k
    return S


def func_j(j, k, i, p):
    f = somatorio(j, k) - (i / p)
    return f


def juros(x, y, z):
    E = 0.000000001
    X1 = 0
    X2 = 0.3 * (z / (x - z))
    X3 = z / (x - z)
    h3 = X3 - X2
    h2 = X2 - X1
    q = h3 / h2
    A = ((q * func_j(X3, y, x, z)) - (q * (1 + q) * func_j(X2, y, x, z)) + (calc_potencia(q, 2) * func_j(X1, y, x, z)))
    B = (((2 * q + 1) * func_j(X3, y, x, z)) - (calc_potencia((1 + q), 2) * func_j(X2, y, x, z)) - (
                calc_potencia(q, 2) * func_j(X1, y, x, z)))
    C = ((1 + q) * func_j(X3, y, x, z))
    Q1 = (- (2 * C / (B + raiz_quadrada(calc_potencia(B, 2) - 4 * A * C))))
    Q2 = (- (2 * C / (B - raiz_quadrada(calc_potencia(B, 2) - 4 * A * C))))
    Qn = 0
    if valor_absoluto(Q1) < valor_absoluto(Q2):
        Qn = Q1
    if valor_absoluto(Q2) < valor_absoluto(Q1):
        Qn = Q2
    X4 = X3 + h3 * Qn
    while erro_relativo(X3, X4) < E or X4 == 0:
        X1 = X2
        X2 = X3
        X3 = X4
        X4 = X3 + h3 * Qn
    print(X4)
    return X4


print(mdc([-5, -70, -500, -5, 0]))
print(simplificar_fracao(7,35))
print(fracao(1.52))
print(raiz_quadrada(100))