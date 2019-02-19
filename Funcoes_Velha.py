class Funcoes(object):
    def ___init__(self):
        pass     

    def InserirPosicao(tab, t):
        # Verifica se a jogada pode ser validada
        
        valid_pos = True
        while valid_pos:

            verif_input = True
            while verif_input:
                l = int(input("Posição na linha: "))
                c = int(input("Posição na coluna: "))

                # VERIFICA SE A POSIÇÃO ESTÁ DENTRO DO INDICE DA MATRIZ (3X3)
                if 0 <= l <= 3 and 0 <= c <= 3:

                    # VERIFICA SE A POSIÇÃO JÁ ESTÁ PREENCHIDA
                    if tab[l][c] != "X" and tab[l][c] != "O":
                        tab[l][c] = t

                        valid_pos = False
                        verif_input = False
                        continue
                    else:
                        print("\nPosição já preenchida! Digite outra posição.\n")
                else:
                    print("\nPosição fora de index! Digite novamente.\n")
            

            print("\n")        
            for i in range(1, 4):
                print(" {} | {} | {} ".format(tab[i - 1][0][0],tab[i - 1][1][0],tab[i - 1][2][0]))
                if i < 3:
                    print("-" * 11)

            print("-"*40)


    def VerifGanhou(tab, nome):
        # Verifica se o jogador venceu após sua jogada
        if (tab[0][0][0] == "X" and tab[0][1][0] == "X" and tab[0][2][0] == "X" or
               tab[1][0][0] == "X" and tab[1][1][0] == "X" and tab[1][2][0] == "X" or
               tab[2][0][0] == "X" and tab[2][1][0] == "X" and tab[2][2][0] == "X" or
               tab[0][0][0] == "X" and tab[1][0][0] == "X" and tab[2][0][0] == "X" or
               tab[0][1][0] == "X" and tab[1][1][0] == "X" and tab[2][1][0] == "X" or
               tab[0][2][0] == "X" and tab[1][2][0] == "X" and tab[2][2][0] == "X" or
               tab[0][0][0] == "X" and tab[1][1][0] == "X" and tab[2][2][0] == "X" or
               tab[2][0][0] == "X" and tab[1][1][0] == "X" and tab[0][2][0] == "X"):
            print("\nParabéns {}!".format(nome))
            quit()

        if (tab[0][0][0] == "O" and tab[0][1][0] == "O" and tab[0][2][0] == "O" or
               tab[1][0][0] == "O" and tab[1][1][0] == "O" and tab[1][2][0] == "O" or
               tab[2][0][0] == "O" and tab[2][1][0] == "O" and tab[2][2][0] == "O" or
               tab[0][0][0] == "O" and tab[1][0][0] == "O" and tab[2][0][0] == "O" or
               tab[0][1][0] == "O" and tab[1][1][0] == "O" and tab[2][1][0] == "O" or
               tab[0][2][0] == "O" and tab[1][2][0] == "O" and tab[2][2][0] == "O" or
               tab[0][0][0] == "O" and tab[1][1][0] == "O" and tab[2][2][0] == "O" or
               tab[2][0][0] == "O" and tab[1][1][0] == "O" and tab[0][2][0] == "O"):
            print("\nParabéns {}!".format(nome))
            quit()
