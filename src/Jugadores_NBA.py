'''
Created on 22 oct. 2021

@author: Matias Angulo Flores'''

import csv
from collections import namedtuple
from datetime import datetime
import matplotlib.pyplot as plt

Registro= namedtuple("Registro", "Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season")
########################################################################################
'''Lee el fichero de entrada
   @param fichero
   @stype nombre del fichero de entrada -> str
   
   .....
   
   @return lista de tuplas jugadores
   @rtype str'''

def lee_jugadores(fichero):
    jugadores=[]
    with open(fichero,encoding="utf-8") as f:
        lector =csv.reader(f)
        next(lector)
        for j in lector :
            j[2] = bool(j[2])
            j[3]= datetime.strptime(j[3], "%b %d, %Y").date()
            j[6] = int(j[6])
            j[7] = int(j[7])
            j[8] = int(j[8])
            j[9] = int(j[9])
            j[11] = int(j[11])
            j[13] = float(j[13])
            j[14] = int(j[14])
            j[15] = int(j[15])
            j[16] = bool(j[16])
            jugadores.append(Registro(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],[15],j[16]))
    
    return jugadores

########################################################################################
'''Calcula el conjunto de equipos presentes en una lista de equipos
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return la lista de equipos ordenadas alfabeticamente
   @rtype str'''

def calcula_equipos(jugadores):
    
    aux = {r.Team for r in jugadores}
    res = sorted(aux,)
    return res

########################################################################################
'''Calcula la suma total de los pesos de un jugador dado
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return total de opercaiones de un nombre
   @rtype int'''

def sumaPeso(jugadores, nombre):
    return sum([r.Weight for r in jugadores if r.Player == nombre])

########################################################################################
'''Calcula el jugador con mayor edad
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return una lista de tuplas con el jugador con mayor edad
   @rtype str'''

def edad_maxima(jugadores):
    maximo = max(jugadores,key = lambda x:x.Age)
    res = [r for r in jugadores if r.Age== maximo.Age]
    return res

########################################################################################
'''Calcula los jugadores con menor edad
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return una lista de tuplas con los jugadores con menor edad
   @rtype str'''

def jugadores_menor_edad(jugadores, Last_Season=1, n=5):
    res = sorted([r for r in jugadores if r.Last_Season== Last_Season], key = lambda x:x.Age)
    return res[:n]

########################################################################################
'''Calcula los jugadores de cada temporada
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return un diccionario ordenado de la temporada mas antigua hasta la mas reciente con los nombres de los jugadores que han participado en esa temporada
   @rtype (int-str)'''
    
def jugadores_por_temporada(jugadores):
    res= dict()
    for r in jugadores:
        if r.Season in res:
            res[r.Season].append(r.Player)
        else:
            res[r.Season]=[r.Player]
    return res

########################################################################################
'''Distribuye los jugadores por sus respectivas edades
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return un diccionario que devuelve la cantidad de jugadores con las diferentes edades
   @rtype int'''
def contar_jugadores_por_edad(jugadores):
    años = {}
    for jug in jugadores:
        if jug.Age not in años:
            años[jug.Age] = 1
        else:
            años[jug.Age]  += 1
    return años

########################################################################################
'''Muestra al equipo con la mayor suma de pesos
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return una tupla con el equipo con mas suma de peso y la suma de pesos de dicho equipo
   @rtype (str-int)'''
def equipo_mas_peso(jugadores):
    dicc = dict()
    for j in jugadores:
        clave=j.Team
        if clave in dicc:
            dicc[clave] += j.Weight
        else:
            dicc[clave] = j.Weight
    return max(dicc.items(), key=lambda x:x[1])

########################################################################################
'''Muestra el porcentaje de cada jugador de la parte de vida que ha estado en la liga
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return un diccionario con clave los nombres de los jugadores y valor los porcentajes de los años que ha estasdo en la liga respecto a su edad
   @rtype (str-float)'''
def porcentaje_de_temporadas_en_liga_por_jugador(jugadores,Player):
    Temporadas_en_liga =0
    Edad_tot =0
    for j in jugadores:
        if Player==j.Player:
            Temporadas_en_liga += j.Seasons_in_league
            Edad_tot += j.Age
    return Temporadas_en_liga*100/Edad_tot

def dicc_porcentaje_de_temporadas_en_liga_por_jugador(jugadores):
    dicc= dict()
    clave = (j.Player for j in jugadores)
    for Player in clave:
        dicc[Player] = porcentaje_de_temporadas_en_liga_por_jugador(jugadores,Player)
    return dicc

########################################################################################
'''Muestra a los jugadores mas jovenes por temporada
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return un diccionario donde las claves son las temporadas y los valores son una lista con los n jugadores de menor edad de cada temporada en forma de tupla (edad, nombre)
   @rtype (int-str)'''
def dicc_n_joven_jugador_por_temporadas(jugadores, n=1):
    claves = sorted({j.Season for j in jugadores})
    dicc = {clave: 0 for clave in claves}
    for key in dicc:
        dicc[key] = sorted([(j.Age, j.Player) for j in jugadores if j.Season ==key])[:n]
    return dicc

########################################################################################
'''Muestra una grafica en funcion al peso y a la edad
   @param jugadores es una lista de tuplas leidos de fichero
   @stype Lista de jugadores(Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season)
   -> [FrecuenciaNombre(str,str,boolean,datetime.date,str,str,int,int,int,int,str,int,str,float,int,int,boolean)]
   
   .....
   
   @return una grafica en funcion al peso y la edad
   @rtype (int-int)'''    
def grafica_peso_edad(jugadores):
    x=Weight
    y=Age
    plt.plot(x,y)