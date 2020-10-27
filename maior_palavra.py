maior = 0
texto = input('=> ').split(" ")


for palavra in texto:
    if len(palavra) > maior:
        maior = len(palavra)

print(maior)
