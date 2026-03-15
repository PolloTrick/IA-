# ==========================================
# REPASO GENERAL: CISCO PYTHON ESSENTIALS
# ==========================================

# --- MÓDULO 1: Fundamentos e Instalación ---
# Python es un lenguaje de ALTO NIVEL e INTERPRETADO por CPython.
print("--- Módulo 1: Hola Mundo y Literales ---")
print("Octal 0o123:", 0o123)       # Base 8
print("Hexa 0x123:", 0x123)         # Base 16
print("Booleano:", True > False)    # True es 1, False es 0

# --- MÓDULO 2: Variables y Operadores ---
print("\n--- Módulo 2: Variables y Aritmética ---")
# Regla de variables: No empezar con números, no espacios, no palabras reservadas.
variable_legal = 10
x, y = 10, 3

print("División Entera (//):", x // y) # Resultado: 3 (suprime decimales)
print("Residuo o Módulo (%):", x % y)  # Resultado: 1 (lo que sobra)
print("Exponente (**):", 2 ** 3)       # Resultado: 8

# Prioridad: () -> ** -> * / // % -> + -
resultado_test = 2 + 3 * 5 ** 2 
# 1. 5**2=25 -> 2. 3*25=75 -> 3. 2+75=77
print("Resultado Prioridad:", resultado_test)

# --- MÓDULO 3: Lógica y Bucles ---
print("\n--- Módulo 3: Control de Flujo ---")
edad = 18
# Condicionales
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor.")

# Listas (Mutables: se pueden cambiar)
frutas = ["Manzana", "Pera", "Piña"]
frutas.append("Uva")     # Agrega al final
del frutas[1]            # Elimina "Pera"
print("Lista de frutas:", frutas)

# Bucles: FOR (sabemos cuántas veces) vs WHILE (hasta que algo cambie)
print("Bucle FOR en rango:")
for i in range(3): # 0, 1, 2
    print(f"  Vuelta {i}")

# --- MÓDULO 4: Funciones, Tuplas y Diccionarios ---
print("\n--- Módulo 4: Estructuras y Funciones ---")

# Función con Retorno y Parámetro
def calcular_iva(precio):
    return precio * 0.16

print("IVA de 100:", calcular_iva(100))

# Tuplas (Inmutables: NO se pueden cambiar)
mi_tupla = (1, 2, 3) 

# Diccionarios (Llave : Valor)
estudiante = {
    "nombre": "Nexus",
    "curso": "Cisco Python",
    "modulo": 4
}
print("Nombre del Diccionario:", estudiante["nombre"])

# ==========================================
# FIN DEL REPASO
# ==========================================