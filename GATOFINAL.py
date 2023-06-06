# Función para imprimir el tablero actualizado
def imprimir_tablero(tablero):
    print("\n")
    for i in range(3):
        print(tablero[i][0] + " | " + tablero[i][1] + " | " + tablero[i][2])
        if i < 2:
            print("---------")
    print("\n")

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    # Comprobación de filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True

    # Comprobación de columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    # Comprobación de diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para jugar al juego
def jugar_tic_tac_toe():
    # Crear el tablero vacío
    tablero = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]

    jugador_actual = "X"
    jugadas = 0

    # Ciclo principal del juego
    while jugadas < 9:
        imprimir_tablero(tablero)

        # Obtener la fila y la columna del jugador
        fila = int(input("Ingresa el número de fila (0-2): "))
        columna = int(input("Ingresa el número de columna (0-2): "))

        # Verificar si la posición está ocupada
        if tablero[fila][columna] != " ":
            print("La posición ya está ocupada. Intenta de nuevo.")
            continue

        # Realizar la jugada
        tablero[fila][columna] = jugador_actual
        jugadas += 1

        # Verificar si el jugador actual ha ganado
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print("¡Jugador", jugador_actual, "ha ganado!")
            return

        # Cambiar al siguiente jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

    # Si no hay ganador después de 9 jugadas, es un empate
    imprimir_tablero(tablero)
    print("¡Es un empate!")

# Iniciar el juego
jugar_tic_tac_toe()


