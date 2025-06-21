laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

camino = [[' ' for _ in range(9)] for _ in range(9)]

movs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def valor(celda):
    if celda in ('I', 'F'):
        return 1
    return celda

def encontrar_inicio():
    for i in range(9):
        for j in range(9):
            if laberinto[i][j] == 'I':
                return i, j
    return None

def buscar(fila, col, puntos):
    if fila < 0 or fila >= 9 or col < 0 or col >= 9:
        return False
    if camino[fila][col] == '$' or valor(laberinto[fila][col]) == 0:
        return False

    if valor(laberinto[fila][col]) in [3, 4]:
        puntos += valor(laberinto[fila][col])

    camino[fila][col] = '$'

    if laberinto[fila][col] == 'F':
        return puntos >= 23

    for dx, dy in movs:
        nueva_fila = fila + dx
        nueva_col = col + dy
        if buscar(nueva_fila, nueva_col, puntos):
            return True

    # No retrocedemos: si se bloquea, termina
    return False

def mostrar(matriz):
    for fila in matriz:
        print(' '.join(str(x) for x in fila))
    print()

def main():
    print("Laberinto original:")
    mostrar(laberinto)

    inicio = encontrar_inicio()
    if not inicio:
        print("No se encontró el punto de inicio.")
        return

    fila_inicio, col_inicio = inicio
    exito = buscar(fila_inicio, col_inicio, 0)

    if exito:
        print("Se encontró un camino con 23 o más puntos.")
    else:
        print("No hay camino válido con suficientes puntos.")

    print("Camino recorrido:")
    mostrar(camino)

main()