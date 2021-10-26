# Proyecto del Primer Cuatrimestre Fundamentos de Programaci�n (Curso 2021/2022)
Autor/a: Mat�as Angulo Flores; uvus: matangflo

Aqui� debes a�adir la descripci�n del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes modulos de Python que conforman el proyecto.
  * **Jugadores_NBA.py**: Este es el modulo principal, donde existen funciones para explotar los datos de los jugadores de NBA
  * **Jugadores_NBA_test.py**: Este es el modulo de pruebas, que contiene funciones de prueba para probar las funciones del modulo principal
  * **\<modulo2.py\>**: Añade descripciones para el resto de modulos que pueda tener tu proyecto. Por ejemplo, sera conveniente tener un modulo separado con funciones genericas para dibujar gr�ficas y/o otro con funciones genericas de conversi�n de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **Dataset_NBA.csv**: Este es el archivo con los datos de jugadores de la NBA
    
## Estructura del *dataset*

Aqui debes describir la estructura del dataset explicando que representan los datos que contiene y la descripci�n de cada una de las columnas.

El dataset esta compuesto por 9 columnas, con la siguiente descripcion:

* **\<columna 1>**: de tipo str, representa al jugador
* **\<columna 2>**: de tipo str, representa al equipo
* **\<columna 3>**: de tipo str, representa la liga oeste o este
* **\<columna 4>**: de tipo date, representa la fecha
* **\<columna 5>**: de tipo str, representa la posicion
* **\<columna 6>**: de tipo str, representa la altura del jugador
* **\<columna 7>**: de tipo int, representa el peso del jugador
* **\<columna 8>**: de tipo int, representa la edad del jugador
* **\<columna 9>**: de tipo int, representa el año de entrada
* **\<columna 10>**: de tipo int, representa las temporadas en la liga
* **\<columna 11>**: de tipo str, representa la temporada
* **\<columna 12>**: de tipo int, representa el año
* **\<columna 13>**: de tipo str, representa el equipo del que proviene
* **\<columna 14>**: de tipo float, representa el valor real
* **\<columna 15>**: de tipo int, representa la altura en centimetros
* **\<columna 16>**: de tipo int, representa el peso en kilogramos
* **\<columna 17>**: de tipo int, representa las temporadas anteriores

## Tipos implementados

Registro=namedtuple("Registro","Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season")

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **lee_jugadores(fichero)**: Lee los datos del fichero csv y devuelve una lista de tuplas con los datos del fichero.
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
