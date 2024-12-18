class Vehiculo:
    def __init__(self, marca: str, modelo: str, nro_ruedas: int):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas


class Automovil(Vehiculo):
    def __init__(
        self,
        marca: str,
        modelo: str,
        nro_ruedas: int,
        velocidad: float,
        cilindrada: float,
    ):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Particular(Automovil):
    def __init__(
        self,
        marca: str,
        modelo: str,
        nro_ruedas: int,
        velocidad: float,
        cilindrada: float,
        nro_puestos: int,
    ):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos


class Carga(Automovil):
    def __init__(
        self,
        marca: str,
        modelo: str,
        nro_ruedas: int,
        velocidad: float,
        cilindrada: float,
        carga: float,
    ):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, tipo: str):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(
        self,
        marca: str,
        modelo: str,
        nro_ruedas: int,
        tipo: str,
        nro_radios: int,
        cuadro: str,
        motor: str,
    ):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
