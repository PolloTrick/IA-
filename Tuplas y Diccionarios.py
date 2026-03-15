# --- SECCIÓN 2: TUPLAS Y DICCIONARIOS ---

# 1. TUPLAS: Son inmutables (no se pueden modificar una vez creadas)
# Se definen con paréntesis ()
coordenadas = (10.5, 20.8)
print("Coordenada X:", coordenadas[0])
# coordenadas[0] = 15.0  <-- Esto daría ERROR en el examen

# 2. DICCIONARIOS: Colecciones de pares Llave:Valor
# Se definen con llaves {}
glosario_cisco = {
    "PCEP": "Certified Entry-Level Python Programmer",
    "IDLE": "Entorno de desarrollo integrado",
    "PEP8": "Guía de estilo para Python"
}

print("\nSignificado de PCEP:", glosario_cisco["PCEP"])

# Añadir o modificar elementos
glosario_cisco["Scope"] = "Alcance de una variable"
print("Glosario actualizado:", glosario_cisco)