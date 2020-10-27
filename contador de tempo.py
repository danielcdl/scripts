'''
# coding: utf-8
from datetime import timedelta

__author__ = "Daniel Chaves de Lima"
__email__ = "danielchaves001@gmail.com"

def fim_experiecia():
    """
        A função lê o horário de inicio de início (formato hh:mm:ss) e a duração (formato hh:mm:ss) de uma experiência.
        O programa retorna o horário(formato hh:mm:ss) do término da mesma.
    """
    while True:
        entrada = input("Digite o horário de inicio da experiência(FORMATO hh:mm:ss): ")
        if entrada.count(":") == 2:
            dados = entrada.split(":")  # cria uma lista com os dados [hh, mm, ss]
            try: # faca primeiro, depois peça desculpas.
                hora = int(dados[0])
                minuto = int(dados[1])
                segundo = int(dados[2])

                inicio = timedelta(hours=hora, minutes=minuto, seconds=segundo)  # transforma para o formato de tempo para o python realizar os cálculos
                break
            except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
                print("Digite números inteiros")
        else:
            print("digite os dados no FORMATO hh:mm:ss")

    while True:
        entrada = input("Digite o tempo de DURAÇÃO da experiência(FORMATO hh:mm:ss): ")
        if entrada.count(":") == 2:
            dados = entrada.split(":")  # cria uma lista com os dados [hh, mm, ss]
            try: # faca primeiro, depois peça desculpas.
                hora = int(dados[0])
                minuto = int(dados[1])
                segundo = int(dados[2])

                duracao = timedelta(hours=hora, minutes=minuto, seconds=segundo)  # transforma para o formato de tempo para o python realizar os cálculos
                break
            except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
                print("Digite números inteiros")
        else:
            print("digite os dados no FORMATO hh:mm:ss")
    return inicio + duracao


fim = fim_experiecia()
dados = str(fim).split(":")
print("a experiência terá fim as {} horas,{} minutos e {} segundos".format(dados[0], dados[1], dados[2]))



# coding: utf-8
from datetime import timedelta

__author__ = "Daniel Chaves de Lima"
__email__ = "danielchaves001@gmail.com"


def fim_experiecia():
    """
        A função lê o horário de inicio de início (formato hh:mm:ss) e a duração (em segundos) de uma experiência.
        O programa retorna o horário(formato hh:mm:ss) do término da mesma.
    """
    while True:
        entrada = input('Digite o horário de inicio da experiência(HORAS): ')
        try:  # faca primeiro, depois peça desculpas.
            hora = int(entrada)
            break
        except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
            print("Digite números inteiros")
    while True:
        entrada = input("Digite o horário de inicio da experiência(MINUTOS): ")
        try:  # faca primeiro, depois peça desculpas.
            minuto = int(entrada)
            break
        except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
            print("Digite números inteiros")
    while True:
        entrada = input('Digite o horário de inicio da experiência(SEGUNDOS):')
        try:  # faca primeiro, depois peça desculpas.
            segundo = int(entrada)
            break
        except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
            print("Digite números inteiros")

    inicio = timedelta(hours=hora, minutes=minuto,
                       seconds=segundo)  # transforma para o formato de tempo para o python realizar os cálculos

    while True:
        entrada = input('Digite o tempo de DURAÇÃO da experiência(em segundos):')
        try:  # faca primeiro, depois peça desculpas.
            duracao = int(entrada)
            duracao = timedelta(seconds=duracao)
            break
        except ValueError:  # caso os valores não sejam inteiros. (as desculpas. kkkk)
            print("Digite números inteiros")

    return inicio + duracao


fim = fim_experiecia()
dados = str(fim).split(":")
print("a experiência terá fim as {} horas,{} minutos e {} segundos".format(dados[0], dados[1], dados[2]))

'''


def fah(c):
    return (1.8 * c) + 32


def kel(c):
    return c + 273


lista = []
i = 1
while len(lista) < 5:
    try: # Caso a entrada não seja um numero real o programa avisa ao invés de parar
        c = float(input("{} - Digite um número de graus Celsius: ".format(i)))  # substituir virgula por ponto!
        lista.append([c, fah(c), kel(c)])
        i += 1
    except ValueError:
        print("valor INCORRETO")
print("""
__________________________________________
 Nº    Celsius     Fahrenheit      Kelvin 
------------------------------------------""")
for i in range(5):
    print("""|%s|   %.2f        %.2f          %.2f """ %(str(i + 1) + ".", lista[i][0], lista[i][1], lista[i][2]))
print("------------------------------------------")
