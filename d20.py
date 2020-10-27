import random

# RPG busca pela água
print('você é uma pessoa que vaga pelo reino de wanana. Você sente sede!')

vida = 100
while vida > 0:
    print('Escolha o que deseja fazer:')
    escolha = input('digite 1 para beber água no rio ou \ndigite 2 para beber água de um cacto na sua frente.\n')

    if escolha == '1':
        print('A água do rio é suja.')
        escolha2 = input('Deseja beber a água: digite 1 pra sim ou 2 para não\n')
        if escolha2 == '1':
            print('Você se deu bem e não esta mais com sede, porém você acaba tendo diarreia.')
            print('Prescisa tirar um numero maior que 10 no D20 para se curar. Role o d20')
            while True:
                input('aperte enter para rolar o d20')
                d20 = random.randint(1, 20)
                print(f"D20: {d20}")
                if d20 < 10:
                    print('você da azar e acaba morrendo de desidratação')
                    vida -= 40
                    print(f'vida: {vida}')
                    if vida <= 0:
                        print('que pena, você morreu')
                        break
                else:
                    print(
                        'Que sorte, você tirou um numero maior que 10, portanto esta curado.\nBoa viagem pelo reino de wanana.')
                    break
            break

        elif escolha2 == '2':
            print('você morreu de sede.')
            vida = 0

    elif escolha == '2':
        print('você tenta quebrar o cacto.')
        cacto = random.randint(1, 2)
        if cacto == 1:
            print('o cacto era venenoso Pe voce se feri, adquirindo uma infecção.')
            print('uma voz te chama ao longe')
            escolha1 = input('faça sua escolha deseja segui-la? : sim ou não')
            if escolha1 == 'sim':
                print('você acaba encontrando uma bruxa, que te mata.')
                vida = False
            elif escolha1 == 'não':
                print('Ainda bem, você bebe a água. Ainda está com infecção.')
                print('você pode comer um cogumelo ou ir no rio lavar a ferida.')
                escolha3 = input('Esolha:cogumelo ou rio')
                if escolha3 == 'cogumelo':
                    print('Você esta livre da infecção e pode viver feliz')
                    print('WIN.')
                    vida = True
                elif escola3 == 'rio':
                    print('O rio estava sujo e sua infecção acaba piorando e te levando a morte.')
                    print('LOSE')
                vida = False
        elif cacto == 2:
            print('Você quebra o cacto com um chute e bebe a água, matando sua sede.')
    else:
        print("Opção inválida")

if vida > 0:
    print('Voce venceu o jogo parabens, até a proxima. TO BE CONTINUED...')
else:
    print('Voce perdeu o jogo, até a proxima. TO BE CONTINUED...')