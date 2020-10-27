def comparar(self, evento):
    self.comparacao = self.en_nascimento.get()


def on_write(self, *args):
    s = self.var.get()

    if len(s) > 0:
        k = ""
        for caractere in s:
            if caractere.isdigit():
                k += caractere

        g = ""
        i = 0
        mudanca = False
        for caractere in self.comparacao:
            if caractere.isdigit():
                g += caractere

                if len(k) <= len(g):
                    break
                if not k[i] == g[i]:
                    k = k[:i + 1] + k[i + 2:]
                    mudanca = True
                    break
                i += 1
        self.formatar_data(k, i, mudanca)


def formatar_data(self, data, indice, mudar):
    if 2 < len(data) < 5:
        self.en_nascimento.delete(0, END)
        self.en_nascimento.insert(0, data[:2] + "/" + data[2:])
    elif len(data) >= 5:
        self.en_nascimento.delete(0, END)
        self.en_nascimento.insert(0, data[:2] + "/" + data[2:4] + "/" + data[4:8])
    else:
        self.en_nascimento.delete(0, END)
        self.en_nascimento.insert(0, data)
    if mudar:
        if indice < 2:
            self.en_nascimento.icursor(indice + 1)
        elif indice == 2 or indice == 3:
            self.en_nascimento.icursor(indice + 2)
        else:
            self.en_nascimento.icursor(indice + 3)