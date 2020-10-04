lista = []
while True:
    try:  # verifica se a entrada é válida
        n = (int(input('Digite um número inteiro: ')))
        if n <= 0:
            break
        lista.append(n)
    except ValueError:
        print('O valor digitado não é inteiro. Tente Novamente')

quantidade_entradas = len(lista)
media = sum(lista) / quantidade_entradas

lista = sorted(lista)
posicao = int(quantidade_entradas / 2)
if quantidade_entradas % 2 == 1:
    mediana = lista[posicao]
else:
    mediana = (lista[posicao - 1] + lista[posicao]) / 2

chaves = set(lista)  # cria um conjunto com os valores da entrada. sem valores repetidos
quantidades = {}
for chave in chaves:  # cria um dicionario com a quantida de entradas para cada valor
    quantidades[chave] = lista.count(chave)

valor_moda = max(quantidades.values())
moda = []
for chave in chaves:
    if quantidades[chave] == valor_moda:
        moda.append(chave)

print(lista)
print(f'A media dos números digitados é: {media}.')
print(f'A mediana dos números digitados é: {mediana}.')
print(f'A moda dos números digitados é: {moda}.')
