class Motor():
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, nregistro: int):
        self.registro = nregistro
    def asignarTipo(self, ntipo: str):
        if ntipo == "electrico" or ntipo == "electrico":
            self.tipo = ntipo