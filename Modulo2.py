# --- 1. VARIABLES Y ASIGNACIÓN ---
# Las variables son cajas con nombre. Aquí creamos una entera y una flotante.
n_manzanas = 5          # Integer (Entero)
precio_manzana = 1.5    # Float (Flotante/Decimal)

# Operación simple y guardado en nueva variable
costo_total = n_manzanas * precio_manzana
print("Costo total de las manzanas:", costo_total)

# --- 2. OPERADORES ARITMÉTICOS (Lo que más preguntan en Cisco) ---
# Ojo con la jerarquía de operaciones: (), **, (* / // %), (+ -)

x = 10
y = 3

print("\n--- Operaciones con", x, "y", y, "---")
print("Suma:", x + y)           # 13
print("Exponente:", x ** y)     # 10 elevado a 3 = 1000
print("División clásica:", x / y) # Siempre devuelve un FLOAT (3.333)
print("División entera:", x // y) # Corta los decimales (devuelve 3)
print("Módulo (Residuo):", x % y) # Lo que sobra de la división (1)

# --- 3. ATAJOS DE OPERACIÓN (Operadores compuestos) ---
# En lugar de x = x + 1, usamos:
x += 1 
print("\nNuevo valor de x después de x += 1:", x) # Ahora vale 11

# --- 4. TRABAJANDO CON STRINGS (Cadenas) ---
nombre = "Python"
version = "3.12"
# Concatenación (unir textos)
print("\nEstás aprendiendo " + nombre + " versión " + version)
# Replicación (multiplicar texto)
print("Cisco " * 3) # Imprime Cisco Cisco Cisco 

# --- 5. ENTRADA DE DATOS (Función input) ---
# IMPORTANTE: input() siempre devuelve un STRING. 
# Hay que convertirlo (casting) si queremos hacer cálculos.
print("\n--- Sección Interactiva ---")
usuario = input("Dime tu nombre: ")
edad = int(input("¿Cuántos años tienes? ")) # Convertimos el texto a número entero

print("Hola " + usuario + ", el próximo año tendrás", edad + 1, "años.")