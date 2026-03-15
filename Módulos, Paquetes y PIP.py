# --- MÓDULO 1: MODULARIDAD ---
import math          # Importar un módulo completo
from sys import path # Importar solo una propiedad específica
import time as t     # Usar un alias (apodo)

# PIP: Es la herramienta para instalar paquetes de terceros
# Comando en consola: pip install pandas (por ejemplo)

print("Directorio de búsqueda de Python:", path[0])
print("Calculando seno de 90°:", math.sin(math.pi/2))