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
    if celda == 'I' or celda == 'F':
        return 1
    else:
        return celda
def buscar(fila, col, puntos):
    if fila < 0 or fila >= 9 or col < 0 or col >= 9:
        return False
    if camino[fila][col] == '$' or valor(laberinto[fila][col]) == 0:
        return False
    if valor(laberinto[fila][col]) in [3, 4]:
        puntos += valor(laberinto[fila][col])    
    camino[fila][col] = '$'
    if laberinto[fila][col] == 'F':
        if puntos >= 23:
            return True
        else:
            camino[fila][col] = ' '
            return False

    
    for dx, dy in movs:
        nueva_fila = fila + dx
        nueva_col = col + dy
        if buscar(nueva_fila, nueva_col, puntos):
            return True

    camino[fila][col] = ' '
    return False
def encontrar_inicio():
    for i in range(9):
        for j in range(9):
            if laberinto[i][j] == 'I':
                return i, j
    return None
def mostrar(matriz):
    for fila in matriz:
        print(' '.join(str(x) for x in fila))
    print()
def main():
    print("Laberinto original:")
    mostrar(laberinto)

    inicio = encontrar_inicio()
    if not inicio:
        print("No se encontró la casilla inicial 'I'.")
        return
    fila_inicio, col_inicio = inicio
    exito = buscar(fila_inicio, col_inicio, 0)
    if exito:
        print("¡Camino encontrado con 23 puntos o más!")
    else:
        print("No se encontró un camino válido con suficientes puntos.")
    print("Camino recorrido (marcado con $):")
    mostrar(camino)


main()