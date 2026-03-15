# --- MÓDULO 3: CLASES Y OBJETOS ---

class Robot:
    poblacion = 0  # Variable de clase (común a todos)

    def __init__(self, nombre):
        self.nombre = nombre  # Variable de instancia (única de cada robot)
        Robot.poblacion += 1
        
    def saludar(self):
        print(f"Hola, soy el robot {self.nombre}")

# Herencia
class RobotCombate(Robot):
    def atacar(self):
        print(f"{self.nombre} está disparando!")

mi_bot = RobotCombate("R-01")
mi_bot.saludar()
mi_bot.atacar()