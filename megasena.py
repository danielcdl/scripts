import random


def entrada_int(mensagem):
    """
    valida a entrada para que a mesma seja um numero inteiro
    :return: numero inteiro
    """
    while True:
        try:  # tenta converter a entrada para inteiro
            entrada = int(input(mensagem + "\n"))
            break  # se digitar um numero interio interrompe o laço
        except ValueError:  # se o numero não for inteiro
            print('Digite um número inteiro')
    return entrada


def sortear():
    """
    função que sortea numeros aleatoriamente entre 1 e 60
    :return: lista de numeros sorteado
    """
    sorteio = []
    cont = 0
    while cont < 6:
        numero = random.randint(1, 61)  # 1 <= numero <61
        if numero not in sorteio:
            sorteio.append(numero)
            cont += 1
    return sorted(sorteio)


jogos = entrada_int('Quantos jogos você deseja fazer? ')  # garante que seja um numero inteiro
cont = 1
listaCompleta = []
while cont <= jogos:
    # se usar aspas tripla tudo fica com a formatacao deixada
    print("""
Valores dos jogos:
6 números = R$ 4,50
7 números = R$ 31,50
8 números = R$ 126,00
    """)

    numero = entrada_int(f'Quantos números de 1 a 60 você gostaria jogar no {cont}º jogo?')
    lista = []
    if 6 <= numero < 9:
        cont2 = 0
        while cont2 < numero:
            print(f'Escolha o {cont2 + 1}º número.')
            num = int(input())

            if 1 <= num <= 60:
                if num not in lista:
                    lista.append(num)
                    cont2 += 1
                else:
                    print('Não pode repetir os números, escolha outro.')
            else:
                print('Não encontrei o número na tabela, escolha outro.')
        lista = sorted(lista)
        print(f'Esses foram os números escolhidos: {lista}. Boa sorte!!')
        listaCompleta.append(lista)
        cont += 1
    else:
        print('Não existe esse valor de jogo. Selecione a quantidade de jogos desejada')

megasena = sortear()
print('sorteado: ', megasena)
for bilhete in listaCompleta:
    print(bilhete)
    if set(bilhete) == set(megasena):
        print('Parabéns ao novo milionário')
    else:
        print('Não foi dessa vez')
