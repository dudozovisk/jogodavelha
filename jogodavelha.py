matriz_jogo=[[0,0,0],
             [0,0,0],
             [0,0,0]]


jogadas=[1,2,3,4,5,6,7,8,9]
while True:

    jogA = int(input("Digite a sua jogada, Jogador A: "))
    if jogA not in jogadas:
        jogA = int(input("Digite novamente a sua jogada, Jogador A: "))
    if jogA == 1:
        jogadas.remove(1)
        matriz_jogo[0][0] = "X"
    if jogA == 2:
        jogadas.remove(2)
        matriz_jogo[0][1] = "X"
    if jogA == 3:
        jogadas.remove(3)
        matriz_jogo[0][2] = "X"
    if jogA == 4:
        jogadas.remove(4)
        matriz_jogo[1][0] = "X"
    if jogA == 5:
        jogadas.remove(5)
        matriz_jogo[1][1] = "X"
    if jogA == 6:
        jogadas.remove(6)
        matriz_jogo[1][2] = "X"
    if jogA == 7:
        jogadas.remove(7)
        matriz_jogo[2][0] = "X"
    if jogA == 8:
        jogadas.remove(8)
        matriz_jogo[2][1] = "X"
    if jogA == 9:
        jogadas.remove(9)
        matriz_jogo[2][2] = "X"

    if matriz_jogo[0][0] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][2] and matriz_jogo[0][0] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[0][2] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][0] and matriz_jogo[0][2] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[0][0] == matriz_jogo[0][1] and matriz_jogo[0][1] == matriz_jogo[0][2] and matriz_jogo[0][0] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[1][0] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[1][2] and matriz_jogo[1][0] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[2][0] == matriz_jogo[2][1] and matriz_jogo[2][1] == matriz_jogo[2][2] and matriz_jogo[2][0] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[0][0] == matriz_jogo[1][0] and matriz_jogo[1][0] == matriz_jogo[2][0] and matriz_jogo[0][0] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[0][1] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][1] and matriz_jogo[0][1] != 0:
        print("Jogador A venceu!!!")
        break
    if matriz_jogo[0][2] == matriz_jogo[1][2] and matriz_jogo[1][2] == matriz_jogo[2][2] and matriz_jogo[0][2] != 0:
        print("Jogador A venceu!!!")
        break
    
    
    print(matriz_jogo)
    print(f"Essas são as jogadas disponíveis: {jogadas}")
    
    
    
    
    if len(jogadas)==0:
        print("Empatou, talvez na próxima :( ")
        
        break


    jogB = int(input("Digite a sua jogada, Jogador B: "))
    if jogB not in jogadas:
        jogB = int(input("Digite novamente a sua jogada, Jogador B: "))
    if jogB == 1:
        jogadas.remove(1)
        matriz_jogo[0][0] = "O"
    if jogB == 2:
        jogadas.remove(2)
        matriz_jogo[0][1] = "O"
    if jogB == 3:
        jogadas.remove(3)
        matriz_jogo[0][2] = "O"
    if jogB == 4:
        jogadas.remove(4)
        matriz_jogo[1][0] = "O"
    if jogB == 5:
        jogadas.remove(5)
        matriz_jogo[1][1] = "O"
    if jogB == 6:
        jogadas.remove(6)
        matriz_jogo[1][2] = "O"
    if jogB == 7:
        jogadas.remove(7)
        matriz_jogo[2][0] = "O"
    if jogB == 8:
        jogadas.remove(8)
        matriz_jogo[2][1] = "O"
    if jogB == 9:
        jogadas.remove(9)
        matriz_jogo[2][2] = "O"
    
    
    
    if matriz_jogo[0][0] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][2] and matriz_jogo[0][0] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[0][2] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][0] and matriz_jogo[0][2] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[0][0] == matriz_jogo[0][1] and matriz_jogo[0][1] == matriz_jogo[0][2] and matriz_jogo[0][0] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[1][0] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[1][2] and matriz_jogo[1][0] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[2][0] == matriz_jogo[2][1] and matriz_jogo[2][1] == matriz_jogo[2][2] and matriz_jogo[2][0] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[0][0] == matriz_jogo[1][0] and matriz_jogo[1][0] == matriz_jogo[2][0] and matriz_jogo[0][0] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[0][1] == matriz_jogo[1][1] and matriz_jogo[1][1] == matriz_jogo[2][1] and matriz_jogo[0][1] != 0:
        print("Jogador B venceu!!!")
        break
    if matriz_jogo[0][2] == matriz_jogo[1][2] and matriz_jogo[1][2] == matriz_jogo[2][2] and matriz_jogo[0][2] != 0:
        print("Jogador B venceu!!!")
        break

    print(matriz_jogo)
    print(f"Essas são as jogadas disponíveis: {jogadas}")
