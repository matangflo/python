'''
Created on 22 oct. 2021

@author: Matias Angulo Flores 
'''
from Jugadores_NBA import *
jugadores = lee_jugadores('../data/Dataset_NBA.csv')

###############################################################
#Funciones auxiliares
###############################################################
def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 
        
###############################################################
#Funciones de test
###############################################################

def test_lee_jugadores():                         # Test de la funcion lee_jugadores
    lista_jugadores=lee_jugadores("C:/Users/USUARIO/git/proyecto-entregable-python-matangflo/data/Dataset_NBA.csv")
    print("Hay",len (lista_jugadores), "jugadores")
    print("3 primeros jugadores",lista_jugadores[:3])
    print("3 ultimos jugadores",lista_jugadores[-3:])


def test_calcula_equipos():         # Test de la función calcula_equipos
    equipos = calcula_equipos(jugadores)
    print("Equipos:")
    print("Hay " , len (equipos), "equipos diferentes")
    mostrar_numerado(equipos)


def test_sumaPeso():                # Test de la funcion sumaPeso
    print("El total de peso del jugador es:")
    print(sumaPeso(jugadores, "LeBron James"))
    

def test_edad_maxima():             # Test de la funcion edad_maxima
    print("El jugador con mayor edad es:")
    print(edad_maxima(jugadores))


def test_jugadores_menor_edad(Last_Season=1, n=5):   # Test de la funcion jugadores_menor_edad
    res = jugadores_menor_edad(jugadores, Last_Season, n)
    print( f"Los {n} jugadores de la ultima temporada {Last_Season} con menor edad son:" )
    mostrar_numerado(res)


def test_jugadores_por_temporada():             # Test de la funcion jugadores_por_temporada
    dic = jugadores_por_temporada(jugadores)
    claves_ordenadas =sorted(dic)
    for clave in claves_ordenadas:
        print(clave,"->",dic[clave])


def test_contar_jugadores_por_edad():             # Test de la funcion contar_jugadores_por_edad
    res = contar_jugadores_por_edad(jugadores)
    print("Todos los jugadores distribuidos por sus edades:")
    print(res)
    
    
def test_equipo_mas_peso():             # Test de la funcion equipo_mas_peso
    res = equipo_mas_peso(jugadores)
    print("El equipo con mas suma de pesos es:")
    print(res)
    
    
def test_dicc_porcentaje_de_temporadas_en_liga_por_jugador():             # Test de la funcion dicc_porcentaje_de_temporadas_en_liga_por_jugador
    res = dicc_porcentaje_de_temporadas_en_liga_por_jugador(jugadores)
    print("Los porcentajes de cada jugador son:")
    print(res)
    
    
def test_dicc_n_joven_jugador_por_temporadas(n=1):             # Test de la funcion dicc_n_joven_jugador_por_temporadas
    res = dicc_n_joven_jugador_por_temporadas(jugadores, n)
    print("Los jugadores mas jovenes de cada temporada son:")
    print(res)


def test_grafica_peso_edad():             # Test de la funcion grafica_peso_edad
    res = grafica_peso_edad(jugadores)
    plt.show(res) 


if __name__=="__main__":
    
################################################################
#  Programa principal
################################################################
    test_lee_jugadores()
    #test_calcula_equipos()
    #test_sumaPeso()
    #test_edad_maxima()
    #test_jugadores_menor_edad()
    #+test_jugadores_por_temporada()
    #test_contar_jugadores_por_edad()
    #test_equipo_mas_peso()
    #test_dicc_porcentaje_de_temporadas_en_liga_por_jugador()
    #test_dicc_n_joven_jugador_por_temporadas()
    #grafica_peso_edad()