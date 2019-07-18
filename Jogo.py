from Funcoes_Velha  import Funcoes

# TUTORIAL
print("=" * 15)
print("{:^15}".format("POSIÇÕES"))
print("=" * 15)

print("""\n    0   1   2
0     |   |   
   -----------
1     |   |   
   -----------
2     |   |   \n""")

print("=" * 15)
# FIM TUTORIAL


j1_nome = input("\nNome 1º jogador: ").strip().title()
j2_nome = input("Nome 2º jogador: ").strip().title()

tab = [[["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]], [["-"], ["-"], ["-"]]]

# JOGADAS
jogo = True
jogadas = 1
while jogo and jogadas <= 9:
    rodada = True
    while rodada:

        # VEZ DO JOGADOR 1
        verif_1 = True
        while verif_1:
            print("\nSua vez {}".format(j1_nome))
            tipo = "X"

            Funcoes.InserirPosicao(t=tipo, tab=tab)
            if jogadas>= 5:
                Funcoes.VerifGanhou(tab=tab, nome=j1_nome)
                  
            verif_1 = False

        jogadas += 1

        # VERIFICAÇÃO DE FIM DE JOGO
        if jogadas >= 9:
            print("VELHA! NINGUÉM GANHOU.")
            break

        # VEZ DO JOGADOR 2
        verif_2 = True
        while verif_2:
            print("\nSua vez {}".format(j2_nome))
            tipo = "O"

            Funcoes.InserirPosicao(t=tipo, tab=tab)
            if jogadas >= 5:
                Funcoes.VerifGanhou(tab=tab, nome=j1_nome)

            verif_2 = False
        jogadas += 1

        rodada = False
