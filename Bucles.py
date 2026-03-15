# --- SECCIÓN 2: BUCLES Y REPETICIONES ---

# 1. Bucle WHILE (Mientras la condición sea cierta)
secreto = "cisco123"
intento = ""

print("\n--- Bloque de seguridad ---")
while intento != secreto:
    intento = input("Introduce la contraseña para salir del bucle: ")
    if intento != secreto:
        print("Error. Inténtalo de nuevo.")

print("¡Acceso concedido!")

# 2. Bucle FOR con range() (Ideal para contar)
print("\n--- Cuenta regresiva con FOR ---")
# range(inicio, fin_sin_incluir, paso)
for i in range(5, 0, -1):
    print("Lanzamiento en:", i)

print("¡Despegue! 🚀")

# Punto clave de Cisco: 'break' sale del bucle, 'continue' salta a la siguiente vuelta.