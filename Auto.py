from Asiento import Asiento
from Motor import Motor
class Auto():
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo= modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos():
        contador = 0
        if self.asientos != None:
            for elemento in self.asientos:
                if elemento is not None:
                    contador += 1
        return contador
    def verificarIntegridad():
        if Asiento.registro == Auto.registro and Auto.registro == Motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"

