tab = [["-", "-", "-"],
       ["-", "-", "-"],
       ["-", "-", "-"]]

class Funcoes:
    def __init__(self, cod):
        self.cod = cod
        self.nome = input("Digite seu nome: ").strip()

        if self.cod == 1:
            self.simbolo = 'x'
        else:
            self.simbolo = 'o'

    def exibirTabela(self):
        for linha in range(0, len(tab)):
            for coluna in range(0, len(tab[linha])):
                print(tab[linha][coluna], end="")

                if coluna == 0 or coluna == 1:
                    print(" | ", end="")

            if linha == 0 or linha == 1:
                print("\n----------")

    def exibirNome(self):
        return self.nome

    def verifFim(self):
        for linha in range(0, 3):
            if tab[linha][0] == self.simbolo and tab[linha][1] == self.simbolo and tab[linha][2] == self.simbolo:
                return True

        for coluna in range(0, 3):
            if tab[0][coluna] == self.simbolo and tab[1][coluna] == self.simbolo and tab[2][coluna] == self.simbolo:
                return True

        if tab[0][0] == self.simbolo and tab[1][1] == self.simbolo and tab[2][2] == self.simbolo or\
                tab[0][2] == self.simbolo and tab[1][1] == self.simbolo and tab[2][0] == self.simbolo:
            return True

    def inserirPosicao(self, linha, coluna):
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tab[linha][coluna] != "-":
            print("Posição inválida\n")
            return True

        else:
            tab[linha][coluna] = self.simbolo
            return False
