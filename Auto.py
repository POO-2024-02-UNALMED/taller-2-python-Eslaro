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

    def cantidadAsientos(self):
        contador = 0
        if self.asientos != None:
            for Asiento in self.asientos:
                if Asiento != None:
                    contador += 1
        return contador

    def verificarIntegridad(self):
        if self.motor == None or self.asientos == None:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if asiento != None and (asiento.registro!= self.registro or self.motor.registro != self.registro):
                return "Las piezas no son originales"

        return "Auto Original"
            

