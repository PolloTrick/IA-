# --- SECCIÓN 3: LISTAS Y LÓGICA ---

# Creación de una lista de dispositivos de red
dispositivos = ["Router", "Switch", "Hub", "PC"]

# Acceder a elementos (Recuerda: ¡Empezamos a contar desde 0!)
print("Primer dispositivo:", dispositivos[0]) 

# Operaciones lógicas combinadas
es_admin = True
tiene_permisos = False

# Operador AND: Ambos deben ser True
# Operador OR: Al menos uno debe ser True
if es_admin or tiene_permisos:
    print("\nAcceso al panel de configuración permitido.")

# Manipulación básica de listas
dispositivos.append("Servidor") # Agrega al final
del dispositivos[2]             # Elimina el 'Hub' que ya es viejo
print("Lista actualizada:", dispositivos)
print("Total de dispositivos:", len(dispositivos))