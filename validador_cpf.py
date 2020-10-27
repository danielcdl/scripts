soma = 0

#validador do formato do cpf
while True:
    cpf = input("Digite o CPF: ")

    # remover pontos e traços
    if '.' in cpf:
        cpf = cpf.replace('.', '')
    if '-' in cpf:
        cpf = cpf.replace('-', '')

    if len(cpf) == 11:
        inteiros = True
        try:
            int(cpf)
            break
        except ValueError:
            print("CPF Inválido, tente novamente")
    else:
        print("CPF Inválido, tente novamente")

# itera duas listas, uma com os 9 primeiros digitos do cpf e outra com os numeros
# de 10 até 2
for digito, i in zip(cpf[:9], range(10, 1, -1)):

    print("CPF", digito, "*", i, "=", int(digito) * i)
    soma += int(digito) * i

    print("Soma da validação ", soma)

validacao1 = (soma * 10) / 11 # INÚTIL

print("Resultado da ((primeira soma * 10)/11) = ", validacao1)

resto_validacao1 = (soma * 10) % 11

print("Resto da primeira validação: ", resto_validacao1)

if resto_validacao1 == 10:
    resto_validacao1 = 0

if resto_validacao1 != (int(cpf[9])):
    print("CPF invalido..")

else:
    print("Validação confirmada!!")

    soma = 0

    # itera duas listas, uma com os 10 primeiros digitos do cpf e outra com os numeros
    # de 11 até 2
    for digito, i in zip(cpf[:10], range(11, 1, -1)):
        print("CPF ", digito, "Multiplicador", i, "resulta", int(digito) * i)
        soma += int(digito) * i

    print("Soma da segunda verificação: ", soma)

    validacao2 = (soma * 10) / 11

    print("Resultado da segunda soma ", validacao2)

    resto_validacao2 = (soma * 10) % 11

    if resto_validacao2 == 10:
        resto_validacao2 = 0

    print("Resto da segunda verificação: ", resto_validacao2)

    if resto_validacao2 == int(cpf[10]):
        print("Validação confirmada!")

    else:
        print("CPF invalido. Por favor informe outro CPF...")
