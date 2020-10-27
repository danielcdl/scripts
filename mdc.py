numeros = []

def mdc_euclides(numeros:list):
    a = numeros[0]
    for i in range(1, len(numeros)):
        b = numeros[i]

        if a >= b:
            dividendo = a
            divisor = b
        else:
            dividendo = b
            divisor = a

        resto = dividendo % divisor
        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo % divisor
        a = divisor
    return a

while True:
    entrada = input('digite um numero inteiro ou "s" pra sair: ')
    if entrada. upper() != "S":
        try:
            if entrada != "0":
                numeros.append(int(entrada))
            else:
                print("0 não pode ser usado!!!") 
        except ValueError:
            print("digite um valor inteiro!!")
    else:
        break

if len(numeros) >= 2:
    mdc = mdc_euclides(numeros)
    print("O mdc de", end=" ")
    for numero in numeros[:-1]:
        print(numero, end=", ")
    print(numeros[-1], "é", mdc)
else:
    print("Você deveria ter digitado mais de um número")
