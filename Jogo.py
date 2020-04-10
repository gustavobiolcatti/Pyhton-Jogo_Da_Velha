from Funcoes_Velha import Funcoes as velha

players = (velha(1), velha(2))

print("\n\n************** AVISO *************")
print("As linhas e colunas vão de 1 até 3\n")

players[0].exibirTabela()

print("\n**********************************\n")

for i in range(1, 5):
    for player in players:
        while True:
            print("\nSua vez ", player.exibirNome())
            linha = int(input("Insira a linha: ")) - 1
            coluna = int(input("Insira a coluna: ")) - 1

            verif_jogada = player.inserirPosicao(linha, coluna)

            if not verif_jogada:
                print("")
                player.exibirTabela()
                break

        if player.verifFim():
            print("\n\nParabéns {}, você ganhou!!".format(player.exibirNome()))
            break

    if player.verifFim():
        break
