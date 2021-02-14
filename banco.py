notas = [100, 50, 20, 10, 5, 2, 1]

while True:
    valor_saque = input('Qual o valor que gostaria de sacar? R$ ')
    if valor_saque.isdigit():
        valor_saque = int(valor_saque)
        quantidade_notas = {}
        valor = valor_saque
        for nota in notas:
            quantidade = 0
            while valor >= nota:
                valor -= nota
                quantidade += 1
            if quantidade > 0:
                quantidade_notas[nota] = quantidade
        print(quantidade_notas)
    else:
        print('digite um valor inteiro')
    