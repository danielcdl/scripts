def nova_matriz():
	print("Digite os caracteres separados por espaço e ao teminar digite \"fim\"")
	matriz = []
	while True:
		linha = input(f"digite os caracteres da {len(matriz)+1}ª linha ou \"fim\" para encerrar: ")
		if linha.upper() == 'FIM':
			break
		else:
			matriz.append(linha.split(" "))
	return matriz

def novas_palavras():
	while True:
		try:
			n = int(input("Digite quantas palavras serão buscadas: "))
			break
		except ValueError:
			print('Digite um numero inteiro!')
	palavras = []
	for i in range(1,n+1):
		palavra = input(f"Digite a {i}ª palavra que se´ra buscada: ")
		palavras.append(palavra)

	return palavras


def achar_palavra(palavra, matriz):
	localizacao = []
	ocorrencias = 0

	# busca inicial
	posicoes_iniciais = []
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == palavra[0] or matriz[i][j] == '*': # caso a palavra comece com *
				posicoes_iniciais.append((i, j))




	for par in posicoes_iniciais:
		# busca horizontal
		encontrada = True
		posicoes = []
		if len(matriz[par[0]]) - par[1] >= len(palavra): # se a palavra couber na linha
			pos = par[1]
			for letra in palavra:
				if letra == matriz[par[0]][pos] or matriz[par[0]][pos] == '*':
					posicoes.append((par[0], pos))
				else:
					encontrada = False
					break
				pos += 1

			if encontrada:
				ocorrencias += 1
				localizacao.extend(posicoes)

		# busca vertial
		encontrada = True
		posicoes = []
		if len(matriz) - par[0] >= len(palavra):  # se a palavra couber na coluna
			pos = par[0]
			for letra in palavra:
				if letra == matriz[pos][par[1]] or matriz[pos][par[1]] == '*':
					posicoes.append((pos, par[1]))
				else:
					encontrada = False
					break
				pos += 1

			if encontrada:
				ocorrencias += 1
				localizacao.extend(posicoes)

		# diagonal cima/baixo

		# diagonal baixo/cima
	print(localizacao)
	return (ocorrencias, localizacao)

def main():
	matriz = nova_matriz()
	palavras = novas_palavras()

	posicoes = []
	for palavra in palavras:
		busca = achar_palavra(palavra, matriz)
		ocorrencias = busca[0]
		posicoes.extend(busca[1])
		print("-" * 40)
		print("Lista de Palavras")
		print("-" * 40)

		print("Palavra:", palavra)
		print("Ocorrencias:", ocorrencias)
		print("-" * 40)

	# Impressão da matriz
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if (i, j) in posicoes:
				matriz[i][j] = matriz[i][j].upper()

	for linha in matriz:
		print(' '.join(linha))

if __name__ == '__main__':
    main()