# Proyecto del Primer Cuatrimestre Fundamentos de Programacion (Curso 2021/2022)
Autor: Matias Angulo Flores; uvus: matangflo

## Estructura de las carpetas del proyecto 

* **/src**: Contiene los diferentes modulos de Python que conforman el proyecto.
    * **Jugadores_NBA.py**: Este es el modulo principal, donde existen funciones para explotar los datos de los jugadores de NBA
    * **Jugadores_NBA_test.py**: Este es el modulo de pruebas, que contiene funciones de prueba para probar las funciones del modulo principal
* **/data**: Contiene el dataset o datasets del proyecto
    * **Dataset_NBA.csv**: Este es el archivo con los datos de jugadores de la NBA
    
## Estructura del *dataset*

El dataset esta compuesto por 9 columnas, con la siguiente descripcion:

* **columna 1**: de tipo str, representa al jugador
* **columna 2**: de tipo str, representa al equipo
* **columna 3**: de tipo boolean, representa la conferencia
* **columna 4**: de tipo datetime.date, representa la fecha
* **columna 5**: de tipo str, representa la posicion
* **columna 6**: de tipo str, representa la altura del jugador
* **columna 7**: de tipo int, representa el peso del jugador
* **columna 8**: de tipo int, representa la edad del jugador
* **columna 9**: de tipo int, representa el año de entrada
* **columna 10**: de tipo int, representa las temporadas en la liga
* **columna 11**: de tipo str, representa la temporada
* **columna 12**: de tipo int, representa el año
* **columna 13**: de tipo str, representa el equipo del que proviene
* **columna 14**: de tipo float, representa el valor real
* **columna 15**: de tipo int, representa la altura en centimetros
* **columna 16**: de tipo int, representa el peso en kilogramos
* **columna 17**: de tipo boolean, representa las temporadas anteriores


## Tipos implementados
import csv

from collections import namedtuple

from datetime import datetime

import matplotlib.pyplot as plt

Registro=namedtuple("Registro","Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season")

## Funciones implementadas

Estas son las funciones utilizadas en el proyecto

### \<modulo 1\>

* **lee_jugadores(fichero)**: Lee los datos del fichero csv y devuelve una lista de tuplas con los datos del fichero.
* **calcula_equipos(jugadores)**: Calcula el conjunto de equipos presentes en una lista de equipos
* **sumaPeso(jugadores, nombre)**: Calcula la suma total de los pesos de un jugador dado
* **edad_maxima(jugadores)**: Calcula el jugador con mayor edad
* **jugadores_menor_edad(jugadores, Last_Season=1, n=5)**: Calcula los jugadores con menor edad
* **jugadores_por_temporada(jugadores)**: Calcula los jugadores de cada temporada
* **contar_jugadores_por_edad(jugadores)**: Distribuye los jugadores por sus respectivas edades
* **equipo_mas_peso(jugadores)**: Muestra al equipo con la mayor suma de pesos
* **dicc_porcentaje_de_temporadas_en_liga_por_jugador(jugadores)**: Muestra el porcentaje de cada jugador de la parte de vida que ha estado en la liga
* **dicc_n_joven_jugador_por_temporadas(jugadores, n=1)**: Muestra a los jugadores mas jovenes por temporada
* **grafica_peso_edad(jugadores)**: Muestra una grafica en funcion al peso y a la edad


### \<test modulo 1\>

* **test_lee_jugadores()**: Test de la funcion lee_jugadores
* **test_calcula_equipos()**: Test de la funcion calcula_equipos
* **test_sumaPeso()**: Test de la funcion sumaPeso
* **test_edad_maxima()**: Test de la funcion edad_maxima
* **test_jugadores_menor_edad(Last_Season=1, n=5)**: Test de la funcion jugadores_menor_edad
* **test_jugadores_por_temporada()**: Test de la funcion jugadores_por_temporada
* **test_contar_jugadores_por_edad()**: Test de la funcion contar_jugadores_por_edad
* **test_equipo_mas_peso()**: Test de la funcion equipo_mas_peso
* **test_dicc_porcentaje_de_temporadas_en_liga_por_jugador()**: Test de la funcion dicc_porcentaje_de_temporadas_en_liga_por_jugador
* **test_dicc_n_joven_jugador_por_temporadas(n=1)**: Test de la funcion dicc_n_joven_jugador_por_temporadas
* **test_grafica_peso_edad()**: Test de la funcion grafica_peso_edad