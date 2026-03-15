# --- MÓDULO 2: EXCEPCIONES Y STRINGS ---
try:
    # Intentamos algo peligroso
    division = 10 / 0
except ZeroDivisionError:
    # Si falla, capturamos el error específico
    print("Error: ¡No puedes dividir por cero en el examen de Cisco!")
finally:
    # Esto se ejecuta pase lo que pase
    print("Intento de operación finalizado.")

# Métodos de Cadenas (Strings) - ¡Muy comunes en el examen!
texto = "Cisco2024"
print(texto.isalnum()) # True: porque tiene letras y números
print(texto.isalpha()) # False: porque tiene números, no solo letras