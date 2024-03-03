##matriz bidimensional
matriz = [
    [33, 11, 92],
    [16, 75, 34],
    [99, 28, 7]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    matriz[fila] = bubble_sort(matriz[fila])
    return matriz

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir la fila que se desea ordenar (0, 1 o 2)
fila_a_ordenar = 2

# Ordenar la fila específica de la matriz en orden ascendente
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)