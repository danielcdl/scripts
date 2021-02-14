
# Validador do formato do cpf

def entrada():
    while True:
        cpf = input("Digite o CPF: ")

        # remover pontos e traços
        if '.' in cpf:
            cpf = cpf.replace('.', '')
        if '-' in cpf:
            cpf = cpf.replace('-', '')

        if len(cpf) == 11:
            try:
                int(cpf)
                return cpf
            except ValueError:
                print("CPF Inválido, tente novamente")
        else:
            print("CPF Inválido, tente novamente")

def validar(cpf):

    soma = 0
    for digito, i in zip(cpf[:9], range(10, 1, -1)):
        soma += int(digito) * i

    digito1 = (soma * 10) % 11

    if digito1 == 10:
        digito1 = 0

    if digito1 == (int(cpf[9])):
        soma = 0
        for digito, i in zip(cpf[:10], range(11, 1, -1)):
            soma += int(digito) * i

        digito2 = (soma * 10) % 11

        if digito2 == 10:
            digito2 = 0

        if digito2 == int(cpf[10]):
            return True

    return False

if __name__ == '__main__':
    cpf = entrada()
    valido = validar(cpf)
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    if valido:
        print(f'O CPF {cpf} é válido')
    else:
        print(f'O CPF {cpf} é inválido')