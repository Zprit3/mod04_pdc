# SISTEMA DE CONTROL DE VEHÍCULOS

## DESCRIPCIÓN

El Equipo de desarrollo de software se reúne con la finalidad de discutir lo referente al diseño de
un sistema para el control de vehículos en un sistema de peaje. Según lo conversado con el
cliente, se tienen los primeros datos:

1. Un vehículo contiene los siguientes atributos: marca, modelo y número de ruedas.
2. Un automóvil contiene los siguientes atributos: marca, modelo, número de ruedas,
   velocidad y cilindrada.

## Diagramas

### Diagrama de Clases (Parte 1)

````mermaid
classDiagram
    class Vehiculo {
        - marca: str
        - modelo: str
        - nro_ruedas: int
    }

    class Automovil {
        - marca: str
        - modelo: str
        - nro_ruedas: int
        - velocidad: float
        - cilindrada: float
    }

    Vehiculo <|-- Automovil

    class Particular {
        - nro_puestos: int
    }

    class Carga {
        - carga: float
    }

    Automovil <|-- Particular
    Automovil <|-- Carga

    class Bicicleta {
        - tipo: str
    }

    Vehiculo <|-- Bicicleta

    class Motocicleta {
        - nro_radios: int
        - cuadro: str
        - motor: str
    }

    Bicicleta <|-- Motocicleta

```mermaid
classDiagram
    class Vehiculo {
        - marca: str
        - modelo: str
        - nro_ruedas: int
    }

    class Automovil {
        - marca: str
        - modelo: str
        - nro_ruedas: int
        - velocidad: float
        - cilindrada: float
    }

    Vehiculo <|-- Automovil

    class Particular {
        - nro_puestos: int
    }

    class Carga {
        - carga: float
    }

    Automovil <|-- Particular
    Automovil <|-- Carga

    class Bicicleta {
        - tipo: str
    }

    Vehiculo <|-- Bicicleta

    class Motocicleta {
        - nro_radios: int
        - cuadro: str
        - motor: str
    }

    Bicicleta <|-- Motocicleta

    class RegistroVehiculos {
        - vehiculos: list
        + registrar_vehiculo(vehiculo)
        + consultar_vehiculos()
        + consultar_por_tipo(tipo)
    }

    RegistroVehiculos --> Vehiculo
````
