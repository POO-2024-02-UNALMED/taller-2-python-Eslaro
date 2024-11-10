class Asiento():
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, ncolor: str):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if ncolor in colores:
            self.color = ncolor
            return True
        else:
            return False