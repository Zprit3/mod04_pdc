import csv
from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
from registro_vehiculos import RegistroVehiculos  # Importamos la clase RegistroVehiculos

def guardar_en_csv(vehiculos, filename="vehiculos.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Marca", "Modelo", "Nro_Ruedas", "Tipo", "Velocidad", "Cilindrada", "Nro_Puestos", "Carga", "Bicicleta_Tipo", "Nro_Radios", "Cuadro", "Motor"])
        for vehiculo in vehiculos:
            if isinstance(vehiculo, Automovil):
                writer.writerow([vehiculo.marca, vehiculo.modelo, vehiculo.nro_ruedas, "Automovil", vehiculo.velocidad, vehiculo.cilindrada, "", "", "", "", "", ""])
            elif isinstance(vehiculo, Particular):
                writer.writerow([vehiculo.marca, vehiculo.modelo, vehiculo.nro_ruedas, "Particular", vehiculo.velocidad, vehiculo.cilindrada, vehiculo.nro_puestos, "", "", "", "", ""])
            elif isinstance(vehiculo, Carga):
                writer.writerow([vehiculo.marca, vehiculo.modelo, vehiculo.nro_ruedas, "Carga", vehiculo.velocidad, vehiculo.cilindrada, "", vehiculo.carga, "", "", "", ""])
            elif isinstance(vehiculo, Bicicleta):
                writer.writerow([vehiculo.marca, vehiculo.modelo, vehiculo.nro_ruedas, "Bicicleta", "", "", "", "", vehiculo.tipo, "", "", ""])
            elif isinstance(vehiculo, Motocicleta):
                writer.writerow([vehiculo.marca, vehiculo.modelo, vehiculo.nro_ruedas, "Motocicleta", "", "", "", "", "", vehiculo.nro_radios, vehiculo.cuadro, vehiculo.motor])

def cargar_desde_csv(filename="vehiculos.csv"):
    vehiculos = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                tipo = row[3]
                marca = row[0]
                modelo = row[1]
                nro_ruedas = int(row[2])
                if tipo == "Automovil":
                    velocidad = float(row[4])
                    cilindrada = float(row[5])
                    vehiculos.append(Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada))
                elif tipo == "Particular":
                    velocidad = float(row[4])
                    cilindrada = float(row[5])
                    nro_puestos = int(row[6])
                    vehiculos.append(Particular(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos))
                elif tipo == "Carga":
                    velocidad = float(row[4])
                    cilindrada = float(row[5])
                    carga = float(row[7])
                    vehiculos.append(Carga(marca, modelo, nro_ruedas, velocidad, cilindrada, carga))
                elif tipo == "Bicicleta":
                    tipo_bicicleta = row[8]
                    vehiculos.append(Bicicleta(marca, modelo, nro_ruedas, tipo_bicicleta))
                elif tipo == "Motocicleta":
                    nro_radios = int(row[9])
                    cuadro = row[10]
                    motor = row[11]
                    vehiculos.append(Motocicleta(marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor))
    except FileNotFoundError:
        print(f"El archivo {filename} no se encontró.")
    return vehiculos


def main():
    registro = RegistroVehiculos()
    vehiculos_cargados = cargar_desde_csv() 
    for vehiculo in vehiculos_cargados:
        registro.registrar_vehiculo(vehiculo)

    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    vehiculo1 = Vehiculo("Genérica", "Modelo X", 4)
    automovil1 = Automovil("Toyota", "Corolla", 4, 180.0, 1.8)
    particular1 = Particular("Chevrolet", "Spark", 4, 160.0, 1.2, 5)
    carga1 = Carga("Mercedes-Benz", "Actros", 8, 120.0, 12.0, 15000)
    bicicleta1 = Bicicleta("Giant", "Escape 3", 2, "Urbana")
    motocicleta1 = Motocicleta("Yamaha", "R3", 2, "Deportiva", 32, "Aluminio", "321cc")
    
    registro.registrar_vehiculo(particular)
    registro.registrar_vehiculo(carga)
    registro.registrar_vehiculo(bicicleta)
    registro.registrar_vehiculo(motocicleta)

    registro.registrar_vehiculo(vehiculo1)
    registro.registrar_vehiculo(automovil1)
    registro.registrar_vehiculo(particular1)
    registro.registrar_vehiculo(carga1)
    registro.registrar_vehiculo(bicicleta1)
    registro.registrar_vehiculo(motocicleta1)

    print("\nTodos los vehículos registrados:")
    for vehiculo in registro.consultar_vehiculos():
        print(vars(vehiculo))

    print("\nConsulta por tipo (automovil):")
    for vehiculo in registro.consultar_por_tipo("Automovil"):
        print(vars(vehiculo))

    print("\nConsulta por tipo (motocicleta):")
    for vehiculo in registro.consultar_por_tipo("Motocicleta"):
        print(vars(vehiculo))

    cantidad = int(input("\n¿Cuántos vehículos desea insertar? "))
    for i in range(cantidad):
        print(f"\nDatos del vehículo {i + 1}")
        marca = input("Inserte la marca del vehículo: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        tipo = input(
            "Inserte el tipo de vehículo (automovil, bicicleta, etc.): "
        ).lower()

        if tipo == "automovil":
            velocidad = float(input("Inserte la velocidad en km/h: "))
            cilindrada = float(input("Inserte el cilindraje en cc: "))
            vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        elif tipo == "bicicleta":
            bicicleta_tipo = input("Inserte el tipo de bicicleta: ")
            vehiculo = Bicicleta(marca, modelo, nro_ruedas, bicicleta_tipo)
        elif tipo == "motocicleta":
            nro_radios = int(input("Inserte el número de radios: "))
            cuadro = input("Inserte el tipo de cuadro: ")
            motor = input("Inserte el tipo de motor: ")
            vehiculo = Motocicleta(
                marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor
            )
        else:
            print("Tipo de vehículo no reconocido.")
            continue

        registro.registrar_vehiculo(vehiculo)

    guardar_en_csv(registro.consultar_vehiculos())

    print("\nVehículos registrados después de la inserción:")
    for vehiculo in registro.consultar_vehiculos():
        print(vars(vehiculo))


if __name__ == "__main__":
    main()
