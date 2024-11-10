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
        for asiento in self.asientos:
            if asiento!= None:
                if asiento.registro == registro and registro == motor.registro:
                    continue
                else:
                    "Las piezas no son originales"
        return "Auto Original"
            

