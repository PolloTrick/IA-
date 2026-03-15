# --- MÓDULO 4: ARCHIVOS Y LAMBDAS ---

# Funciones Lambda (Funciones anónimas de una línea)
sumar = lambda a, b: a + b
print("Suma con lambda:", sumar(5, 10))

# Procesamiento de archivos
try:
    # 'rt' significa Read Text (leer texto)
    with open("datos.txt", "rt") as archivo:
        contenido = archivo.read()
        print(contenido)
except IOError:
    print("Error: No se encontró el archivo.")

# Comprensión de listas (List Comprehension)
cuadrados = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
print("Lista de cuadrados:", cuadrados)