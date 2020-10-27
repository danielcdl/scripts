def mudancaDeBase (n,base):
    conversao = []
    while n != 0:
        resto = n % base
        conversao.append(resto)
        n = int((n - resto)/base)
    return conversao
