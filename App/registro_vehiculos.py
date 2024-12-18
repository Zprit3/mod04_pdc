import csv
from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

class RegistroVehiculos:
    def __init__(self):
        self.vehiculos = []  # Lista para almacenar todos los vehículos registrados

    def registrar_vehiculo(self, vehiculo):
        """
        Registra un vehículo en el sistema.
        """
        if isinstance(vehiculo, Vehiculo):  # Verifica que sea una instancia válida
            self.vehiculos.append(vehiculo)
            print(f"Vehículo registrado: {vehiculo.marca} {vehiculo.modelo}")
        else:
            raise TypeError("El objeto no es un vehículo válido.")

    def consultar_vehiculos(self):
        """
        Retorna todos los vehículos registrados.
        """
        return self.vehiculos

    def consultar_por_tipo(self, tipo: str):
        """
        Retorna los vehículos filtrados por el tipo de clase.
        """
        return [vehiculo for vehiculo in self.vehiculos if type(vehiculo).__name__.lower() == tipo.lower()]

    def guardar_datos_csv(self, nombre_archivo="vehiculos.csv"):
        """
        Guarda los datos de los vehículos en un archivo CSV.
        """
        try:
            with open(nombre_archivo, mode='w', newline='') as archivo:
                archivo_csv = csv.writer(archivo)
                for vehiculo in self.vehiculos:
                    # Guardamos el nombre de la clase y los atributos del vehículo
                    archivo_csv.writerow([str(type(vehiculo)), str(vars(vehiculo))])
            print(f"Datos guardados correctamente en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    def leer_datos_csv(self, nombre_archivo="vehiculos.csv"):
        """
        Lee los datos de los vehículos desde un archivo CSV y los imprime.
        """
        try:
            with open(nombre_archivo, mode='r') as archivo:
                archivo_csv = csv.reader(archivo)
                for fila in archivo_csv:
                    if len(fila) > 1:  # Para evitar líneas vacías
                        clase_vehiculo = fila[0]
                        atributos_vehiculo = eval(fila[1])  # Convierte la cadena del diccionario en un objeto
                        print(f"\nLista de Vehículos {clase_vehiculo.split('.')[-1]}")
                        print(atributos_vehiculo)
        except Exception as e:
            print(f"Error al leer los datos desde el archivo: {e}")
