import random
#juego del gato

gato = [] #matriz que va a contener lo valores del juego

def juegoGato():
    ganador = False
    gato = crearMatriz(3,3,"-")
    formatearMatriz(gato)
    numturnos = 1 #total de turnos que se pueden realizar en una partida
    libre = False
    fil = 0
    col = 0
    jugador = "X"

    if numturnos>9:
        print("¡Es un empate!")
        while ganador==False or numturnos < 9:
            
            #turno del jugador (X)
            #el jugador debe indicar fila y columna (posición)
            #preguntar si la posición eligida está libre
            jugador = "X"

            if verificar_ganador(gato, jugador):
                print("\n")
                print("¡Jugador", jugador, "ha ganado!")
                ganador=True
                return ganador

            while jugador == "X":
                print("\n")
                print("Jugador",jugador,"por favor elija una posición a jugar: ")
                print ("Ronda: ",numturnos)
                fil = int(input("F: "))
                col = int(input("C: "))
                libre = posicionLibre (gato,fil,col)
                if libre == True:
                    gato[fil][col] = "X"
                    numturnos += 1
                    jugador = "O"
                    formatearMatriz(gato)
                    break
                else:
                    print("Posición Ocupada")
                    
            if verificar_ganador(gato, jugador):
                print("\n")
                print("¡Jugador", jugador, "ha ganado!")
                ganador=True
                return ganador
            #TURNO JUGADOR (0)
            
            while jugador =="O":
                print("\n")
                print("Jugado",jugador,"por favor elija una posición a jugar: ")
                print ("Ronda: ",numturnos)
                fil = int(input("F: "))
                col = int(input("C: "))
                libre = posicionLibre (gato,fil,col)
                if libre == True:
                    gato[fil][col] = "0"
                    numturnos += 1
                    jugador = "X"
                    formatearMatriz(gato)
                    break
                else:
                    print("Posición Ocupada")
                    formatearMatriz(gato)

                if verificar_ganador(gato, jugador):
                    print("\n")
                    print("¡Jugador", jugador, "ha ganado!")
                    ganador=True
                    return ganador

        

def posicionLibre(mg,f,c):
    if mg[f][c] == "-":
        return True
    else:
        return False

def crearMatriz(f,c,vi):
    m = []
    for i in range(f):
        m.append([vi]*c)
    return m

def recorrerYCambiar(m,vc): 
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = vc
    return m

def formatearMatriz(m): 
    for i in range(len(m)):
        print()
        for j in range(len(m[0])):
            print(m[i][j], sep="t", end=" ")

def verificar_ganador(gato, jugador):
    # Comprobación de filas
    for i in range(3):
        if gato[i][0] == gato[i][1] == gato[i][2] == jugador:
            return True

    # Comprobación de columnas
    for i in range(3):
        if gato[0][i] == gato[1][i] == gato[2][i] == jugador:
            return True

    # Comprobación de diagonales
    if gato[0][0] == gato[1][1] == gato[2][2] == jugador:
        return True
    if gato[0][2] == gato[1][1] == gato[2][0] == jugador:
        return True

    return False

juegoGato()

#0,0  0,1  0,2
#1,0  1,1  1,2
#2,0  2,1  2,2

