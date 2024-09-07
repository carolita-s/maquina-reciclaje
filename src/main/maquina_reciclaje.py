class MaquinaReciclajeMetales:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

    def clasificar_metales(self, material):
        if "hierro" in material:
            return "Hierro"
        elif "aluminio" in material:
            return "Aluminio"
        else:
            return "Otro"

    def compactar_metales(self, tipo_metal):
        if tipo_metal == "Hierro":
            return "Compactando hierro"
        elif tipo_metal == "Aluminio":
            return "Compactando aluminio"
        else:
            return "Compactando otros metales"

    def calcular_eficiencia(self, cantidad_material, tiempo):
        eficiencia = cantidad_material / tiempo
        return f"Eficiencia: {eficiencia} kg/h"

    def __str__(self):
        return f"Máquina de Reciclaje: {self.nombre}, Capacidad: {self.capacidad} kg"
    