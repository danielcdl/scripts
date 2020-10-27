def ler(Nome_Arq):#recebe o input de 'pasta\nome'
    try:
        banco = open(Nome_Arq+'.shcs','r') #procura por pasta\nome.shcs se n achar da erro o aruivo nessa pasta da error
        banco = banco.read()
        print('leu o arquivo')
    except FileNotFoundError:#então inicia a criação
        try:
            banco = open(Nome_Arq+'.shcs','w') #procura a pasta para criar o arquivo e se nao achar a pasta da error
            banco = banco.write('')
            print('criou o arquivo')
        except FileNotFoundError:
            print('pasta nao encontrada')#e então aqui eu quero parar todo o processo para n ir para o finelly pq la vai procurar o arquivo dnv e vai da error
            input()
            return