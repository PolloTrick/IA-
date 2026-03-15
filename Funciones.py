# --- SECCIÓN 1: FUNCIONES ---

# Definimos una función con un parámetro por defecto
def saludar_estudiante(nombre, curso="Python Essentials"):
    print(f"Hola {nombre}, bienvenido al {curso}.")

# Función que realiza un cálculo y REGRESA un valor
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area  # Es vital para usar el resultado fuera de la función

# Llamadas a las funciones
saludar_estudiante("Nexus")
saludar_estudiante("Juan", "Módulo 4") # Sobrescribimos el parámetro por defecto

resultado = calcular_area_triangulo(10, 5)
print(f"El área calculada es: {resultado}")

# Punto clave Cisco: Las variables creadas dentro de una función 
# son LOCALES y no existen fuera de ella (Scope/Alcance).