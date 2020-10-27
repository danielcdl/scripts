# coding: utf-8
from tkinter import Tk, ttk, StringVar, END, Entry

__author__ = "Daniel Chaves de Lima"
__email__ = "danielchaves001@gmail.com"


class Principal:
    def __init__(self, frame):
        self.var_nome = StringVar()
        self.var_nome.trace("w",
                            self.maiuscula_nome)  # rastrear valor da variavel e executar funcao de validacao quando mudar

        self.en_nome = Entry(root, textvariable=self.var_nome, width=56)
        self.en_nome.bind("<Key>", self.comparar_nome)  # rastreia as entradas
        self.en_nome.place(x=50, y=75)

    #  tive probremas quando usava só a StringVar pois quando havia alteraçoes o cursor se movia sempre para o fim da
    #  entrada então fiz o seguinte:

    def comparar_nome(self, evento):
        """
            Captura a entrada 'self.en_nome' antes que o caractere seja inserido para que se possa comparar e definir
            em qual posicao houve a mudança de caractere. Tambem retorna se foi apertado backspace ou espaço.
        """
        self.comparacao1 = [self.en_nome.get(), evento.char == "\b" or evento.char == ""]

    def maiuscula_nome(self, *args):
        """
            Altera em tempo real a entrada colocando-a em maiuscula.
        """
        s = self.var_nome.get().upper()
        self.en_nome.delete(0, END)
        self.en_nome.insert(0, s)  # caso apenas inserido um caractere no final

        # -- caso o caractere seja modificado em qualquer parte da entrada --
        if len(s) > len(self.comparacao1[0]):
            tamanho = len(self.comparacao1[0])
        else:
            tamanho = len(s)

        for i in range(tamanho):
            if self.comparacao1[0][i] != s[i]:
                # dependendo de qual se for digitado ou o caractere foi apagado, move o cursor pra certa posicao
                if self.comparacao1[1]:
                    self.en_nome.icursor(i)
                else:
                    self.en_nome.icursor(i + 1)
                break


root = Tk()
Principal(root)
root.geometry("{}x{}+{}+{}".format(500, 500, 20, 20))
root.title("ENTRY EM MAIUSCULA")
root.mainloop()

#  caso tenha idéias para melhorar este codigo pode me contatar pelo e-mail do preambulo do código
