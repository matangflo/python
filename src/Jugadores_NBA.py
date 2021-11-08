'''
Created on 22 oct. 2021

@author: Matias Angulo Flores'''

import csv
from collections import namedtuple
from datetime import datetime

Registro= namedtuple("Registro", "Player,Team,Conference,Date,Position,Height,Weight,Age,Draft_year,Seasons_in_league,Season,Season_short,Pre_draft_Team,Real_value,Height_CM,Weight_KG,Last_Season")
########################################################################################

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