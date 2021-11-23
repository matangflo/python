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


if __name__=="__main__":
    
################################################################
#  Programa principal
################################################################
    #test_lee_jugadores()
    #test_calcula_equipos()
    #test_sumaPeso()
    #test_edad_maxima()
    #test_jugadores_menor_edad()
    test_jugadores_por_temporada()