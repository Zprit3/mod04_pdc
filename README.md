### SISTEMA DE CONTROL DE VEHÍCULOS

## DESCRIPCIÓN
El Equipo de desarrollo de software, se reúne con la finalidad de discutir lo referente al diseño de
un sistema para el control de vehículos en un sistema de peaje. Según lo conversado con el
cliente, se tienen los primeros datos:
1. Un vehículo contiene los siguientes atributos: marca, modelo y número de ruedas.
2. Un automóvil contiene los siguientes atributos: marca, modelo, número de ruedas,
velocidad y cilindrada.
En este primer Sprint se acordó con el equipo de desarrollo las siguientes funcionalidades:
Para esta parte, dividen el sprint en:
Parte 1:
● Diseñe el diagrama de clases según los datos capturados con el cliente.

- Solución: 

    classDiagram
    class Vehicle {
        - marca : string
        - modelo : string
        - nro_ruedas : int
    }
    class Automovil {
        - velocidad : int
        - cilindrada : int
    }
    Automovil --|> Vehicle : extends

● Partiendo del diseño de diagrama de clases previamente construido, diseñe en las Clases
en Python.
● Genere tres instancias, y al ejecutar el programa se debe mostrar lo siguiente:

