from random import choice

palavras = ["UVA", "MORANGO", "CUPU"]
palavra_sorteada = choice(palavras)  # sorteia uma palavra da lista
palavra_digitada = len(palavra_sorteada) * ["_"]  # cria uma lista com a quantidade de letras da palavra sorteada
letras_digitadas = [] # letras usadas pelo usuario

tentativas = 0  # uma tentativa só é computada se o usuário errar a letra, já pensou se a palavra > 10 caracteres?
while True:
    entrada_usuario = input("Digite uma letra: ").upper().strip()  # recebe a entrada de letra do usuario
    # upper() deixa em maiusula e strip() elimina os espaços em branco antes e depois da palavra
    if len(entrada_usuario) == 1: # o usuario só pode digitar uma letra por vez
        if entrada_usuario not in letras_digitadas: # verifica se o usuario já digitou a letra
            letras_digitadas.append(entrada_usuario) # adiciona a letra digitada as letras já usadas
            if entrada_usuario in palavra_sorteada: #verifica se o usuario acertou
                for i in range(len(palavra_sorteada)): # se o usuario acertou a letra, ela é posicionada em seu devido lugar
                    if palavra_sorteada[i] == entrada_usuario:
                        palavra_digitada[i] = entrada_usuario
                    print(palavra_digitada[i], end=" ")  # mostra cada letra de palavra_digitada e não dá enter no fim
                print()  # dá um enter para não grudar com a palavra acima

                if "_" not in palavra_digitada: # Se completar todas as letras o usuário ganha
                    print("Voce GANHOU!!!")
                    break

                print("Parabens! Você acertou a letra! ", entrada_usuario)
            else:
                print(entrada_usuario)
                print("Voce não acertou a letra.")
                tentativas += 1
        else:
            print("Você já utilizou a letra", entrada_usuario)
    else:
        print("Digite somente uma letra")

    if tentativas > 10: # verifica se o usuário utilizou o maximo de tentativas
        print("PERDEU!! Maximo de tentativas ultrapassado")
        break
