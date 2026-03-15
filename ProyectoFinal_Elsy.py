from random import choice


def mostrar_tablero(tablero):
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def obtener_casillas_disponibles(tablero):
    disponibles = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] not in ("X", "O"):
                disponibles.append((i, j))
    return disponibles


def pedir_movimiento_jugador(tablero):
    while True:
        entrada = input("Selecciona una casilla disponible (1-9): ")

        try:
            numero = int(entrada)
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if numero < 1 or numero > 9:
            print("El número debe estar entre 1 y 9.")
            continue

        fila = (numero - 1) // 3
        columna = (numero - 1) % 3

        if tablero[fila][columna] in ("X", "O"):
            print("Esa casilla ya fue ocupada. Elige otra.")
            continue

        tablero[fila][columna] = "O"
        break


def revisar_ganador(tablero, simbolo):
    for fila in tablero:
        if fila.count(simbolo) == 3:
            return True

    for columna in range(3):
        if tablero[0][columna] == simbolo and tablero[1][columna] == simbolo and tablero[2][columna] == simbolo:
            return True

    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
        return True

    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
        return True

    return False


def movimiento_computadora(tablero):
    libres = obtener_casillas_disponibles(tablero)
    if libres:
        fila, columna = choice(libres)
        tablero[fila][columna] = "X"


def juego_terminado(tablero):
    if revisar_ganador(tablero, "X"):
        mostrar_tablero(tablero)
        print("La computadora ganó la partida.")
        return True

    if revisar_ganador(tablero, "O"):
        mostrar_tablero(tablero)
        print("Ganaste la partida.")
        return True

    if not obtener_casillas_disponibles(tablero):
        mostrar_tablero(tablero)
        print("La partida terminó en empate.")
        return True

    return False


def iniciar_juego():
    tablero = [
        [1, 2, 3],
        [4, "X", 6],
        [7, 8, 9]
    ]

    print("Juego de Tic-Tac-Toe")
    print("Tú juegas con O y la computadora con X.")
    print("La computadora inicia ocupando el centro.\n")

    while True:
        mostrar_tablero(tablero)

        if juego_terminado(tablero):
            break

        pedir_movimiento_jugador(tablero)

        if juego_terminado(tablero):
            break

        movimiento_computadora(tablero)

        if juego_terminado(tablero):
            break


iniciar_juego()
