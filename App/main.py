from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta


def main():
    vehiculos = []
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(cantidad):
        print(f"Datos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, automovil in enumerate(vehiculos, 1):
        print(f"Datos del automóvil {i} : {automovil}")


if __name__ == "__main__":

    # instancias de prueba
    vehiculo = Vehiculo("Genérica", "Modelo X", 4)
    print(vars(vehiculo))

    automovil = Automovil("Toyota", "Corolla", 4, 180.0, 1.8)
    print(vars(automovil))

    particular = Particular("Chevrolet", "Spark", 4, 160.0, 1.2, 5)
    print(vars(particular))

    carga = Carga("Mercedes-Benz", "Actros", 8, 120.0, 12.0, 15000)
    print(vars(carga))

    bicicleta = Bicicleta("Giant", "Escape 3", 2, "Urbana")
    print(vars(bicicleta))

    motocicleta = Motocicleta("Yamaha", "R3", 2, "Deportiva", 32, "Aluminio", "321cc")
    print(vars(motocicleta))
