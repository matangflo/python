'''
Created on 22 oct. 2021

@author: Matias Angulo Flores'''

import csv
from collections import namedtuple
from datetime import datetime

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
   @rtype str'''
    
def jugadores_por_temporada(jugadores):
    res= dict()
    for r in jugadores:
        if r.Season in res:
            res[r.Season].append(r.Player)
        else:
            res[r.Season]=[r.Player]
    return res
