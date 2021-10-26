'''
Created on 22 oct. 2021

@author: Matias Angulo Flores 
'''
from Jugadores_NBA import *
################################################################
def main():
    lista_jugadores=lee_jugadores("C:/Users/USUARIO/git/proyecto-entregable-python-matangflo/data/Dataset_NBA.csv")
    print(len (lista_jugadores))
    print(lista_jugadores[:3])
    print(lista_jugadores[-3:])

if __name__=="__main__":
    main()