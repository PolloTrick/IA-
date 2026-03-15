# --- SECCIÓN 1: CONTROL DE FLUJO CONDICIONAL ---

# Ejemplo: Clasificador de temperatura
temperatura = float(input("Introduce la temperatura actual: "))

if temperatura > 30:
    # Se ejecuta si la condición es verdadera
    print("Hace mucho calor, enciende el ventilador.")
elif temperatura >= 20:
    # Se ejecuta si la anterior fue falsa, pero esta es verdadera
    print("El clima está agradable.")
elif temperatura > 0:
    print("Hace un poco de frío.")
else:
    # Se ejecuta si ninguna de las anteriores se cumplió
    print("¡Cuidado! Está congelando.")

# Punto clave de Cisco: Solo uno de estos bloques se ejecutará.