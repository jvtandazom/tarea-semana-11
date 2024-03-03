# Definir una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, (i, j)  # Devolver True y la posición si se encuentra el valor
    return False, None  # Devolver False si no se encuentra el valor

# Definir el valor a buscar en la matriz
valor_buscar = 5

# Realizar la búsqueda en la matriz
encontrado, posicion = buscar_valor(matriz, valor_buscar)

# Mostrar el resultado de la búsqueda
if encontrado:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion} de la matriz.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
