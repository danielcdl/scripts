def media(amostra: list):
    """
    :param amostra: lista de elementos da amostra
    :return: float
    """
    quantidade_entradas = len(amostra)
    resultado = sum(amostra) / quantidade_entradas
    return resultado


def mediana(amostra: list):
    amostra = sorted(amostra)
    posicao = int(len(amostra) / 2)
    if len(amostra) % 2 == 1:
        resultado = amostra[posicao]
    else:
        resultado = (amostra[posicao - 1] + amostra[posicao]) / 2
    return resultado


def moda(amostra: list):
    chaves = set(amostra)  # cria um conjunto com os valores da entrada. sem valores repetidos
    quantidades = {}
    for chave in chaves:  # cria um dicionario com a quantida de entradas para cada valor
        quantidades[chave] = amostra.count(chave)

    valor_moda = max(quantidades.values())
    resultado = []
    for chave in chaves:
        if quantidades[chave] == valor_moda:
            resultado.append(chave)
    return resultado


def main():
    lista = []
    while True:
        try:  # verifica se a entrada é válida
            n = (input('Digite o valor da amostra ou "fim" para  calcular: '))
            if n.lower() == "fim":
                break
            else:
                lista.append(float(n))
        except ValueError:
            print('O valor digitado não é um número. Tente Novamente')

    lista = sorted(lista)
    print(lista)
    print(f'A media dos números digitados é: {media(lista)}.')
    print(f'A mediana dos números digitados é: {mediana(lista)}.')
    print(f'A moda dos números digitados é: {moda(lista)}.')


if __name__ == "__main__":
    main()
