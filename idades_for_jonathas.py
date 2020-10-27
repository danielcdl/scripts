pessoas = {'F': [], 'M': []}
idades = {'F': [], 'M': []}
sexos = {'F': [], 'M': []}

for c in range(1, 5):
    print(f' {c}² pessoa')
    pessoa = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo M ou F ?: ').upper().strip()
    print(50 * '=-=')

    if sexo == 'F':
        pessoas['F'].append(pessoa)
        idades['F'].append(idade)
        sexos['F'].append(sexo)
    else:
        pessoas['M'].append(pessoa)
        idades['M'].append(idade)
        sexos['M'].append(sexo)

todas_idades = idades['F'] + idades['M']
soma_das_idades = sum(todas_idades)
len_idades = len(todas_idades)
maior_idade_homem = max(idades['M'])
nome_homem_mais_velho = pessoas['M'][idades['M'].index(maior_idade_homem)]
totmulher20 = sum([1 if idade < 20 else 0 for idade in idades['F']])
print(f'A média de idade do grupo é de {soma_das_idades / len_idades}')

print(f'O idade do homem mais velho é {maior_idade_homem} e o nome é {nome_homem_mais_velho}')

print(f'Ao todo temos {totmulher20} mulher(es) com menos de 20 anos')
