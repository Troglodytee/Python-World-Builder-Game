import os
import contextlib
with contextlib.redirect_stdout(None) :
    import pygame
from pygame.locals import *
from random import *

def mouv_blocs() :
    global grille
    global temperature
    temperature = []
    for i in range (6000) :
        temperature += [0]

    for i in range (len(temperature)) :
        if len(grille[i]) == 6 and grille[i][0:5] == "laser" :
            grille[i] = "rien"
        elif len(grille[i]) == 14 and grille[i][0:12] == "pelectricite" or len(grille[i]) == 12 and grille[i][0:10] == "pexplosion" or len(grille[i]) == 6 and grille[i][0:4] == "pfeu" or len(grille[i]) == 8 and grille[i][0:6] == "pglace" :
            if grille[i][len(grille[i])-1] == "1" :
                grille[i] = grille[i][0:len(grille[i])-2]+str(int(grille[i][len(grille[i])-2])+1)+grille[i][len(grille[i])-1]
                if grille[i][len(grille[i])-2] == "9" :
                    grille[i] = grille[i][0:len(grille[i])-1]+"2"
            elif grille[i][len(grille[i])-1] == "2" :
                grille[i] = grille[i][0:len(grille[i])-2]+str(int(grille[i][len(grille[i])-2])-1)+grille[i][len(grille[i])-1]
                if grille[i][len(grille[i])-2] == "0" :
                    grille[i] = grille[i][0:len(grille[i])-1]+"1"

    for i in range (len(grille)-1,-1,-1) :
        if grille[i] == "boue" or grille[i] == "glace" or grille[i] == "graine" or grille[i][0:3] == "hum" or len(grille[i]) >= 5 and grille[i][0:5] == "perso" or grille[i] == "pierre" or grille[i] == "sable" or grille[i] == "terre" or len(grille[i]) == 14 and grille[i][0:12] == "pelectricite" or len(grille[i]) == 12 and grille[i][0:10] == "pexplosion" or len(grille[i]) == 6 and grille[i][0:4] == "pfeu" or len(grille[i]) == 8 and grille[i][0:6] == "pglace" :
            if i < 5900 and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and not ((len(grille[i]) == 4 or len(grille[i]) == 5 or len(grille[i]) == 6) and grille[i][0:3] == "hum") and not (len(grille[i]) == 7 and grille[i][0:5] == "perso") :
                grille[i+100] = grille[i]
                grille[i] = "rien"
            elif i < 5900 and (grille[i] == "boue" or grille[i] == "pierre" or grille[i] == "sable" or grille[i] == "terre" or len(grille[i]) == 14 and grille[i][0:12] == "pelectricite" or len(grille[i]) == 12 and grille[i][0:10] == "pexplosion" or len(grille[i]) == 6 and grille[i][0:4] == "pfeu" or len(grille[i]) == 8 and grille[i][0:6] == "pglace") and (grille[i+100] == "eau" or grille[i+100] == "eau_toxique" or grille[i+100] == "lave" or grille[i+100] == "petrolee" or grille[i+100] == "petrolea" or grille[i+100] == "poison") :
                grille[i],grille[i+100] = grille[i+100],grille[i]
            elif i < 5900 and ((len(grille[i]) == 5 and grille[i][0:3] == "hum" and (grille[i][4] == "1" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i+101] == "rien" or grille[i+101][0:3] == "feu") or grille[i][4] == "2" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i+99] == "rien" or grille[i+99][0:3] == "feu"))) or (len(grille[i]) == 7 and grille[i][6] == "0" and grille[i][0:5] == "perso" and (grille[i][5] == "1" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i+101] == "rien" or grille[i+101][0:3] == "feu") or grille[i][5] == "2" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i+99] == "rien" or grille[i+99][0:3] == "feu")))) :
                if len(grille[i]) == 5 and grille[i][4] == "1" or len(grille[i]) == 7 and grille[i][5] == "1" :
                    for j in range (-1,5,1) :
                        grille[i-j*100] = grille[i-(j+1)*100]
                        grille[(i+1)-j*100] = grille[(i+1)-(j+1)*100]
                    grille[i-500] = "rien"
                    grille[i-499] = "rien"
                elif len(grille[i]) == 5 and grille[i][4] == "2" or len(grille[i]) == 7 and grille[i][5] == "2" :
                    for j in range (-1,5,1) :
                        grille[i-j*100] = grille[i-(j+1)*100]
                        grille[(i-1)-j*100] = grille[(i-1)-(j+1)*100]
                    grille[i-500] = "rien"
                    grille[i-501] = "rien"
            elif i < 5900 and (len(grille[i]) == 5 and grille[i][0:3] == "hum" and (grille[i+100] == "eau" or grille[i+100] == "eau_toxique" or grille[i+100] == "lave" or grille[i+100] == "petrolee" or grille[i+100] == "petrolea" or grille[i+100] == "poison" or grille[i+100] == "vapeur" or grille[i+100] == "gaz" or grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i][4] == "1" and (grille[i+101] == "eau" or grille[i+101] == "eau_toxique" or grille[i+101] == "lave" or grille[i+101] == "petrolee" or grille[i+101] == "petrolea" or grille[i+101] == "poison" or grille[i+101] == "vapeur" or grille[i+101] == "gaz" or grille[i+101] == "rien" or grille[i+101][0:3] == "feu") or grille[i][4] =="2" and (grille[i+99] == "eau" or grille[i+99] == "eau_toxique" or grille[i+99] == "lave" or grille[i+99] == "petrolee" or grille[i+99] == "petrolea" or grille[i+99] == "poison" or grille[i+99] == "vapeur" or grille[i+99] == "gaz" or grille[i+99] == "rien" or grille[i+99][0:3] == "feu")) or len(grille[i]) == 7 and grille[i][6] == "0" and grille[i][0:5] == "perso" and (grille[i+100] == "eau" or grille[i+100] == "eau_toxique" or grille[i+100] == "lave" or grille[i+100] == "petrolee" or grille[i+100] == "petrolea" or grille[i+100] == "poison" or grille[i+100] == "vapeur" or grille[i+100] == "gaz" or grille[i+100] == "rien" or grille[i+100][0:3] == "feu") and (grille[i][5] == "1" and (grille[i+101] == "eau" or grille[i+101] == "eau_toxique" or grille[i+101] == "lave" or grille[i+101] == "petrolee" or grille[i+101] == "petrolea" or grille[i+101] == "poison" or grille[i+101] == "vapeur" or grille[i+101] == "gaz" or grille[i+101] == "rien" or grille[i+101][0:3] == "feu") or grille[i][5] =="2" and (grille[i+99] == "eau" or grille[i+99] == "eau_toxique" or grille[i+99] == "lave" or grille[i+99] == "petrolee" or grille[i+99] == "petrolea" or grille[i+99] == "poison" or grille[i+99] == "vapeur" or grille[i+99] == "gaz" or grille[i+99] == "rien" or grille[i+99][0:3] == "feu"))) :
                if len(grille[i]) == 5 and grille[i][4] == "1" or len(grille[i]) == 7 and grille[i][5] == "1" :
                    for j in range (-1,5,1) :
                        grille[i-j*100],grille[i-(j+1)*100] = grille[i-(j+1)*100],grille[i-j*100]
                        grille[(i+1)-j*100],grille[(i+1)-(j+1)*100] = grille[(i+1)-(j+1)*100],grille[(i+1)-j*100]
                elif len(grille[i]) == 5 and grille[i][4] == "2" or len(grille[i]) == 7 and grille[i][5] == "2" :
                    for j in range (-1,5,1) :
                        grille[i-j*100],grille[i-(j+1)*100] = grille[i-(j+1)*100],grille[i-j*100]
                        grille[(i-1)-j*100],grille[(i-1)-(j+1)*100] = grille[(i-1)-(j+1)*100],grille[(i-1)-j*100]
            elif len(grille[i]) == 5 and grille[i][0:3] == "hum" and grille[i][4] == "1" :
                if i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu") and (grille[i-101] == "rien" or grille[i-101][0:3] == "feu") and (grille[i-201] == "rien" or grille[i-201][0:3] == "feu") and (grille[i-301] == "rien" or grille[i-301][0:3] == "feu") and (grille[i-401] == "rien" or grille[i-401][0:3] == "feu") and (grille[i-501] == "rien" or grille[i-501][0:3] == "feu") :
                    grille[i] += "0"
                    for j in range (6) :
                        grille[(i-1)-j*100] = grille[i-j*100]
                        grille[i-j*100] = grille[(i+1)-j*100]
                        grille[(i+1)-j*100] = "rien"
                elif i-(i//100)*100 > 0 and i > 99 and (grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i-101] == "rien" or grille[i-101][0:3] == "feu") and (grille[i-201] == "rien" or grille[i-201][0:3] == "feu") and (grille[i-301] == "rien" or grille[i-301][0:3] == "feu") and (grille[i-401] == "rien" or grille[i-401][0:3] == "feu") and (grille[i-501] == "rien" or grille[i-501][0:3] == "feu") and (grille[i-601] == "rien" or grille[i-601][0:3] == "feu") :
                    grille[i] += "0"
                    for j in range (5,-1,-1) :
                        grille[(i-1)-(j+1)*100] = grille[i-j*100]
                        grille[i-(j+1)*100] = grille[(i+1)-j*100]
                        grille[i-j*100] = "rien"
                        grille[(i+1)-j*100] = "rien"
                else :
                    grille[i] = grille[i][0:4]+"20"
                    for j in range (6) :
                        grille[i-j*100],grille[(i+1)-j*100] = grille[(i+1)-j*100],grille[i-j*100]
            elif len(grille[i]) == 5 and grille[i][0:3] == "hum" and grille[i][4] == "2" :
                if i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu") :
                    grille[i] += "0"
                    for j in range (6) :
                        grille[(i+1)-j*100] = grille[i-j*100]
                        grille[i-j*100] = grille[(i-1)-j*100]
                        grille[(i-1)-j*100] = "rien"
                elif i-(i//100)*100 < 99 and i > 99 and (grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu") and (grille[i-599] == "rien" or grille[i-599][0:3] == "feu") :
                    grille[i] += "0"
                    for j in range (5,-1,-1) :
                        grille[(i+1)-(j+1)*100] = grille[i-j*100]
                        grille[i-(j+1)*100] = grille[(i-1)-j*100]
                        grille[i-j*100] = "rien"
                        grille[(i-1)-j*100] = "rien"
                else :
                    grille[i] = grille[i][0:4]+"10"
                    for j in range (6) :
                        grille[i-j*100],grille[(i-1)-j*100] = grille[(i-1)-j*100],grille[i-j*100]
            elif i < 5900 and grille[i] == "graine" and grille[i+100] == "boue" :
                grille[i] = "bois6"
                if i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-100][0:3] == "feu") :
                    grille[i-1] = "bois6"
                elif i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i-100][0:3] == "feu") :
                    grille[i+1] = "bois6"
            elif grille[i] == "graine" :
                grille[i] = "rien"
            elif grille[i] == "hum" :
                grille[i] = "rien"
                if i > 599 and i-(i//100)*100 < 99 and (grille[i-500] == "rien" or grille[i-500][0:3] == "feu") and (grille[i-400] == "rien" or grille[i-400][0:3] == "feu") and (grille[i-300] == "rien" or grille[i-300][0:3] == "feu") and (grille[i-200] == "rien" or grille[i-200][0:3] == "feu") and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                    a = randint(1,4)
                    if a == 1 :
                        grille[i] = "hum41"
                        grille[i-100] = "hum4"
                        grille[i-200] = "hum2"
                        grille[i-300] = "hum3"
                        grille[i-400] = "hum2"
                        grille[i-500] = "hum1"
                        grille[i+1] = "hum4"
                        grille[i-99] = "hum4"
                        grille[i-199] = "hum3"
                        grille[i-299] = "hum3"
                        grille[i-399] = "hum1"
                        grille[i-499] = "hum1"
                    elif a == 2 :
                        grille[i] = "hum4"
                        grille[i-100] = "hum4"
                        grille[i-200] = "hum3"
                        grille[i-300] = "hum3"
                        grille[i-400] = "hum1"
                        grille[i-500] = "hum1"
                        grille[i+1] = "hum42"
                        grille[i-99] = "hum4"
                        grille[i-199] = "hum2"
                        grille[i-299] = "hum3"
                        grille[i-399] = "hum2"
                        grille[i-499] = "hum1"
                    elif a == 3 :
                        grille[i] = "hum61"
                        grille[i-100] = "hum6"
                        grille[i-200] = "hum2"
                        grille[i-300] = "hum5"
                        grille[i-400] = "hum2"
                        grille[i-500] = "hum1"
                        grille[i+1] = "hum6"
                        grille[i-99] = "hum6"
                        grille[i-199] = "hum5"
                        grille[i-299] = "hum1"
                        grille[i-399] = "hum1"
                        grille[i-499] = "hum1"
                    elif a == 4 :
                        grille[i] = "hum6"
                        grille[i-100] = "hum6"
                        grille[i-200] = "hum5"
                        grille[i-300] = "hum1"
                        grille[i-400] = "hum1"
                        grille[i-500] = "hum1"
                        grille[i+1] = "hum62"
                        grille[i-99] = "hum6"
                        grille[i-199] = "hum2"
                        grille[i-299] = "hum5"
                        grille[i-399] = "hum2"
                        grille[i-499] = "hum1"
            elif grille[i] == "perso" :
                grille[i] = "rien"
                if i > 599 and i-(i//100)*100 < 99 and (grille[i-500] == "rien" or grille[i-500][0:3] == "feu") and (grille[i-400] == "rien" or grille[i-400][0:3] == "feu") and (grille[i-300] == "rien" or grille[i-300][0:3] == "feu") and (grille[i-200] == "rien" or grille[i-200][0:3] == "feu") and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                    a = randint(1,2)
                    if a == 1 :
                        grille[i] = "perso10"
                        grille[i-100] = "hum9"
                        grille[i-200] = "hum2"
                        grille[i-300] = "hum8"
                        grille[i-400] = "hum2"
                        grille[i-500] = "hum7"
                        grille[i+1] = "hum0"
                        grille[i-99] = "hum9"
                        grille[i-199] = "hum7"
                        grille[i-299] = "hum8"
                        grille[i-399] = "hum1"
                        grille[i-499] = "hum7"
                    elif a == 2 :
                        grille[i] = "hum0"
                        grille[i-100] = "hum9"
                        grille[i-200] = "hum7"
                        grille[i-300] = "hum8"
                        grille[i-400] = "hum1"
                        grille[i-500] = "hum7"
                        grille[i+1] = "perso20"
                        grille[i-99] = "hum9"
                        grille[i-199] = "hum2"
                        grille[i-299] = "hum8"
                        grille[i-399] = "hum2"
                        grille[i-499] = "hum7"

        elif grille[i] == "eau" or grille[i] == "graine" or grille[i] == "lave" or len(grille[i]) >= 8 and grille[i][0:7] == "petrole" or grille[i] == "poison" or grille[i] == "eau_toxique" :
            if i < 5900 and grille[i] == "eau" and grille[i+100] == "terre" :
                grille[i+100] = "boue"
                grille[i] = "rien"
            elif (i >= 5900 or i < 5900 and not grille[i-100] == "rien") and grille[i] == "graine" :
                grille[i] = "rien"
            elif i < 5900 and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu") :
                grille[i+100] = grille[i]
                grille[i] = "rien"
            elif randint(1,2) == 1 :
                if i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu") :
                    grille[i-1] = grille[i]
                    grille[i] = "rien"
                elif i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                    grille[i+1] = grille[i]
                    grille[i] = "rien"
            else :
                if i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                    grille[i+1] = grille[i]
                    grille[i] = "rien"
                elif i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu") :
                    grille[i-1] = grille[i]
                    grille[i] = "rien"

    for i in range (len(grille)) :
        if len(grille[i]) == 7 and grille[i][0:5] == "perso" and not grille[i][6] == "0" :
            if i > 99 and (grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i][5] == "1" and (grille[i-599] == "rien" or grille[i-599][0:3] == "feu") or grille[i][5] == "2" and (grille[i-601] == "rien" or grille[i-601][0:3] == "feu")) :
                grille[i] = grille[i][0:6]+str(int(grille[i][6])-1)
                for j in range (5,-1,-1) :
                    grille[i-(j+1)*100] = grille[i-j*100]
                    if grille[i][5] == "1" :
                        grille[(i+1)-(j+1)*100] = grille[(i+1)-j*100]
                    elif grille[i][5] == "2" :
                        grille[(i-1)-(j+1)*100] = grille[(i-1)-j*100]
                if grille[i][5] == "1" :
                    grille[i+1] = "rien"
                elif grille[i][5] == "2" :
                    grille[i-1] = "rien"
                grille[i] = "rien"
            elif i > 99 and (grille[i-600] == "eau" or grille[i-600] == "eau_toxique" or grille[i-600] == "lave" or grille[i-600] == "petrolee" or grille[i-600] == "petrolea" or grille[i-600] == "poison" or grille[i-600] == "vapeur" or grille[i-600] == "gaz" or grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i][5] == "1" and (grille[i-599] == "eau" or grille[i-599] == "eau_toxique" or grille[i-599] == "lave" or grille[i-599] == "petrolee" or grille[i-599] == "petrolea" or grille[i-599] == "poison" or grille[i-599] == "vapeur" or grille[i-599] == "gaz" or grille[i-599] == "rien" or grille[i-599][0:3] == "feu") or grille[i][5] == "2" and (grille[i-601] == "eau" or grille[i-601] == "eau_toxique" or grille[i-601] == "lave" or grille[i-601] == "petrolee" or grille[i-601] == "petrolea" or grille[i-601] == "poison" or grille[i-601] == "vapeur" or grille[i-601] == "gaz" or grille[i-601] == "rien" or grille[i-601][0:3] == "feu")) :
                grille[i] = grille[i][0:6]+str(int(grille[i][6])-1)
                for j in range (5,0,-1) :
                    grille[i-(j+1)*100],grille[i-j*100] = grille[i-j*100],grille[i-(j+1)*100]
                    if grille[i][5] == "1" :
                        grille[(i+1)-(j+1)*100],grille[(i+1)-j*100] = grille[(i+1)-j*100],grille[(i+1)-(j+1)*100]
                    elif grille[i][5] == "2" :
                        grille[(i-1)-(j+1)*100],grille[(i-1)-j*100] = grille[(i-1)-j*100],grille[(i-1)-(j+1)*100]
                if grille[i][5] == "1" :
                    grille[(i+1)-100],grille[i+1] = grille[i+1],grille[(i+1)-100]
                elif grille[i][5] == "2" :
                    grille[(i-1)-100],grille[i-1] = grille[i-1],grille[(i-1)-100]
                grille[i-100],grille[i] = grille[i],grille[i-100]
            else :
                grille[i] = grille[i][0:6]+"0"

        elif grille[i] == "vapeur" :
            if i > 99 and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") :
                grille[i-100] = grille[i]
                grille[i] = "rien"
            elif i > 99 and (grille[i-100] == "eau" or grille[i-100] == "eau_toxique" or grille[i-100] == "lave" or grille[i-100] == "petrolee" or grille[i-100] == "petrolea" or grille[i-100] == "poison") :
                grille[i],grille[i-100] = grille[i-100],grille[i]
            elif i-(i//100)*100 > 0 and randint(1,2) == 1 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu") :
                grille[i-1] = grille[i]
                grille[i] = "rien"
            elif i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                grille[i+1] = grille[i]
                grille[i] = "rien"

        elif grille[i][0:3] == "feu" :
            if int(grille[i][3]) > 0 :
                if i > 99 and i-(i//100)*100 > 0 and randint(1,2) == 1 :
                    if grille[i-101] == "rien" :
                        grille[i-101] = grille[i][0:3]+str(int(grille[i][3])-1)
                elif i > 99 and i-(i//100)*100 < 99 :
                    if grille[i-99] == "rien" :
                        grille[i-99] = grille[i][0:3]+str(int(grille[i][3])-1)
                if i > 99 and i-(i//100)*100 < 99 and randint(1,2) == 1 :
                    if grille[i-99] == "rien" :
                        grille[i-99] = grille[i][0:3]+str(int(grille[i][3])-1)
                elif i > 99 and i-(i//100)*100 > 0 :
                    if grille[i-101] == "rien" :
                        grille[i-101] = grille[i][0:3]+str(int(grille[i][3])-1)
                grille[i] = "rien"
            else :
                grille[i] = "rien"

        elif len(grille[i]) == 5 and grille[i][0:4] == "bois" and i > 99 :
            if grille[i][4] == "1" and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") :
                grille[i-100] = "ffeuille2"
            elif grille[i-100] == "rien" or grille[i-100][0:3] == "feu" :
                grille[i-100] = "bois"+str(int(grille[i][4])-1)
            if grille[i] == "bois2" :
                if i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu") :
                    grille[i-1] = "ffeuille3"
                if i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu") :
                    grille[i+1] = "ffeuille3"
            grille[i] = "bois"

        elif len(grille[i]) == 9 and grille[i][0:8] == "ffeuille" :
            if i > 99 :
                if grille[i][8] == "1" and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") :
                    grille[i-100] = "ffeuille"
                elif grille[i][8] == "2" and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") :
                    grille[i-100] = "ffeuille1"
                elif grille[i][8] == "3" :
                    if (grille[i-100] == "rien" or grille[i-100][0:3] == "feu") :
                        grille[i-100] = "ffeuille2"
                    if i-(i//100)*100 > 0 and (grille[i-101] == "rien" or grille[i-101][0:3] == "feu") :
                        grille[i-101] = "ffeuille1"
                    if i-(i//100)*100 < 99 and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu") :
                        grille[i-99] = "ffeuille1"
            grille[i] = "ffeuille"

        elif len(grille[i]) == 13 and grille[i][0:11] == "electricite" :
            if i > 99 and len(grille[i-100]) == 7 and grille[i-100][0:5] == "lampe" :
                grille[i-100] = "lampeo4"
            if i-(i//100)*100 < 99 and len(grille[i+1]) == 7 and grille[i+1][0:5] == "lampe" :
                grille[i+1] = "lampeo4"
            if i < 5900 and len(grille[i+100]) == 7 and grille[i+100][0:5] == "lampe" :
                grille[i+100] = "lampeo4"
            if i-(i//100)*100 > 0 and len(grille[i-1]) == 7 and grille[i-1][0:5] == "lampe" :
                grille[i-1] = "lampeo4"
            if i > 99 and len(grille[i-100]) == 11 and grille[i-100][0:9] == "radiateur" :
                grille[i-100] = "radiateuro4"
            if i-(i//100)*100 < 99 and len(grille[i+1]) == 11 and grille[i+1][0:9] == "radiateur" :
                grille[i+1] = "radiateuro4"
            if i < 5900 and len(grille[i+100]) == 11 and grille[i+100][0:9] == "radiateur" :
                grille[i+100] = "radiateuro4"
            if i-(i//100)*100 > 0 and len(grille[i-1]) == 11 and grille[i-1][0:9] == "radiateur" :
                grille[i-1] = "radiateuro4"
            if i > 99 and len(grille[i-100]) == 15 and grille[i-100][0:13] == "refrigirateur" :
                grille[i-100] = "refrigirateuro4"
            if i-(i//100)*100 < 99 and len(grille[i+1]) == 15 and grille[i+1][0:13] == "refrigirateur" :
                grille[i+1] = "refrigirateuro4"
            if i < 5900 and len(grille[i+100]) == 15 and grille[i+100][0:13] == "refrigirateur" :
                grille[i+100] = "refrigirateuro4"
            if i-(i//100)*100 > 0 and len(grille[i-1]) == 15 and grille[i-1][0:13] == "refrigirateur" :
                grille[i-1] = "refrigirateuro4"
            j = 0
            if i > 99 and len(grille[i-100]) >= 8 and grille[i-100][0:5] == "porte" :
                grille[i-100] = "porte6"+str(grille[i-100][6:len(grille[i-100])])
                j = -100
            if i-(i//100)*100 < 99 and len(grille[i+1]) >= 8 and grille[i+1][0:5] == "porte" :
                grille[i+1] = "porte6"+str(grille[i+1][6:len(grille[i+1])])
                j = 1
            if i < 5900 and len(grille[i+100]) >= 8 and grille[i+100][0:5] == "porte" :
                grille[i+100] = "porte6"+str(grille[i+100][6:len(grille[i+100])])
                j = 100
            if i-(i//100)*100 > 0 and len(grille[i-1]) >= 8 and grille[i-1][0:5] == "porte" :
                grille[i-1] = "porte6"+str(grille[i-1][6:len(grille[i-1])])
                j = -1
            if not j == 0 :
                if grille[i+j][6] == "1" :
                    for k in range (1,int(grille[i+j][7:len(grille[i+j])])+1) :
                        grille[i+j-100*k] = "rien"
                elif grille[i+j][6] == "2" :
                    for k in range (1,int(grille[i+j][7:len(grille[i+j])])+1) :
                        grille[i+j+k] = "rien"
                elif grille[i+j][6] == "3" :
                    for k in range (1,int(grille[i+j][7:len(grille[i+j])])+1) :
                        grille[i+j+100*k] = "rien"
                elif grille[i+j][6] == "4" :
                    for k in range (1,int(grille[i+j][7:len(grille[i+j])])+1) :
                        grille[i+j-k] = "rien"
            if grille[i][11] == "m" :
                if i > 99 and grille[i-100] == "metal" and not grille[i][12] == "3" :
                    grille[i-100] = grille[i][0:12]+"10"
                if i-(i//100)*100 < 99 and grille[i+1] == "metal" and not grille[i][12] == "4" :
                    grille[i+1] = grille[i][0:12]+"20"
                if i < 5900 and grille[i+100] == "metal" and not grille[i][12] == "1" :
                    grille[i+100] = grille[i][0:12]+"30"
                if i-(i//100)*100 > 0 and grille[i-1] == "metal" and not grille[i][12] == "2" :
                    grille[i-1] = grille[i][0:12]+"40"
                if i > 99 and (grille[i][12] == "1" or grille[i][12] == "0") and grille[i-100] == "pont" :
                        grille[i-100] = grille[i][0:11]+"p10"
                elif i-(i//100)*100 < 99 and (grille[i][12] == "2" or grille[i][12] == "0") and grille[i+1] == "pont" :
                        grille[i+1] = grille[i][0:11]+"p20"
                elif i < 5900 and (grille[i][12] == "3" or grille[i][12] == "0") and grille[i+100] == "pont" :
                        grille[i+100] = grille[i][0:11]+"p30"
                elif i-(i//100)*100 > 0 and (grille[i][12] == "4" or grille[i][12] == "0") and grille[i-1] == "pont" :
                    grille[i-1] = grille[i][0:11]+"p40"
                grille[i] = "metal"
            else :
                if i > 99 and grille[i][12] == "1" :
                    if grille[i-100] == "metal" :
                        grille[i-100] = grille[i][0:11]+"m10"
                    elif grille[i-100] == "pont" :
                        grille[i-100] = grille[i][0:11]+"p10"
                elif i-(i//100)*100 < 99 and grille[i][12] == "2" :
                    if grille[i+1] == "metal" :
                        grille[i+1] = grille[i][0:11]+"m20"
                    elif grille[i+1] == "pont" :
                        grille[i+1] = grille[i][0:11]+"p20"
                elif i < 5900 and grille[i][12] == "3" :
                    if grille[i+100] == "metal" :
                        grille[i+100] = grille[i][0:11]+"m30"
                    elif grille[i+100] == "pont" :
                        grille[i+100] = grille[i][0:11]+"p30"
                elif i-(i//100)*100 > 0 and grille[i][12] == "4" :
                    if grille[i-1] == "metal" :
                        grille[i-1] = grille[i][0:11]+"m40"
                    elif grille[i-1] == "pont" :
                        grille[i-1] = grille[i][0:11]+"p40"
                grille[i] = "pont"

    for i in range (len(grille)) :
        if len(grille[i]) == 6 and grille[i][0:3] == "hum" :
            grille[i] = grille[i][0:5]

        elif len(grille[i]) == 14 and grille[i][0:11] == "electricite" :
            grille[i] = grille[i][0:13]

    for i in range (len(grille)) :
        if len(grille[i]) >= 5 and grille[i][0:5] == "multi" :
            if len(grille[i]) == 5 :
                if i > 99 and not grille[i-100] == "rien" and not grille[i-100][0:5] == "multi" and not (len(grille[i-100]) >= 8 and grille[i-100][0:5] == "porte") and not (len(grille[i-100]) >= 4 and grille[i-100][0:3] == "hum") :
                    if not grille[i-100][0:3] == "feu" :
                        grille[i] = grille[i]+grille[i-100]
                    else :
                        grille[i] = grille[i]+"feu2"
                elif i-(i//100)*100 < 99 and not grille[i+1] == "rien" and not grille[i+1][0:5] == "multi" and not (len(grille[i+1]) >= 8 and grille[i+1][0:5] == "porte") and not (len(grille[i+1]) >= 4 and grille[i+1][0:3] == "hum") :
                    if not grille[i+1][0:3] == "feu" :
                        grille[i] = grille[i]+grille[i+1]
                    else :
                        grille[i] = grille[i]+"feu2"
                elif i < 5900 and not grille[i+100] == "rien" and not grille[i+100][0:5] == "multi" and not (len(grille[i+100]) >= 8 and grille[i+100][0:5] == "porte") and not (len(grille[i+100]) >= 4 and grille[i+100][0:3] == "hum") :
                    if not grille[i+100][0:3] == "feu" :
                        grille[i] = grille[i]+grille[i+100]
                    else :
                        grille[i] = grille[i]+"feu2"
                elif i-(i//100)*100 > 0 and not grille[i-1] == "rien" and not grille[i-1][0:5] == "multi" and not (len(grille[i-1]) >= 8 and grille[i-1][0:5] == "porte") and not (len(grille[i-1]) >= 4 and grille[i-1][0:3] == "hum") :
                    if not grille[i-1][0:3] == "feu" :
                        grille[i] = grille[i]+grille[i-1]
                    else :
                        grille[i] = grille[i]+"feu2"
            else :
                possib = []
                if i > 99 and grille[i-100] == "rien" :
                    possib += [-100]
                if i > 99 and i-(i//100)*100 < 99 and grille[i-99] == "rien" :
                    possib += [-99]
                if i-(i//100)*100 < 99 and grille[i+1] == "rien" :
                    possib += [1]
                if i < 5900 and i-(i//100)*100 < 99 and grille[i+101] == "rien" :
                    possib += [101]
                if i < 5900 and grille[i+100] == "rien" :
                    possib += [100]
                if i < 5900 and i-(i//100)*100 > 0 and grille[i+99] == "rien" :
                    possib += [99]
                if i-(i//100)*100 > 0 and grille[i-1] == "rien" :
                    possib += [-1]
                if i > 99 and i-(i//100)*100 > 0 and grille[i-101] == "rien" :
                    possib += [-101]
                if len(possib) > 0 :
                    grille[i+possib[randint(0,len(possib)-1)]] = grille[i][5:len(grille[i])]

    for i in range (len(grille)) :
        if len(grille[i]) == 7 and grille[i][0:6] == "lampeo" :
            grille[i] = grille[i][0:6]+str(int(grille[i][6])-1)
            if grille[i][6] == "0" :
                grille[i] = "lampef0"
        elif len(grille[i]) == 11 and grille[i][0:10] == "radiateuro" :
            grille[i] = grille[i][0:10]+str(int(grille[i][10])-1)
            if grille[i][10] == "0" :
                grille[i] = "radiateurf0"
        elif len(grille[i]) == 15 and grille[i][0:14] == "refrigirateuro" :
            grille[i] = grille[i][0:14]+str(int(grille[i][14])-1)
            if grille[i][14] == "0" :
                grille[i] = "refrigirateurf0"
        elif len(grille[i]) == 9 and grille[i][0:8] == "petrolea" :
            grille[i] = grille[i][0:8]+str(int(grille[i][8])-1)
            if grille[i][8] == "0" :
                grille[i] = "rien"

        elif len(grille[i]) == 5 and grille[i][0:4] == "pile" :
            if grille[i][4] == "3" :
                if i > 99 and grille[i-100] == "metal" :
                    grille[i-100] = "electricitem1"
                elif i > 99 and grille[i-100] == "pont" :
                    grille[i-100] = "electricitep1"
                if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                    grille[i+1] = "electricitem2"
                elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                    grille[i+1] = "electricitep2"
                if i < 5900 and grille[i+100] == "metal" :
                    grille[i+100] = "electricitem3"
                elif i < 5900 and grille[i+100] == "pont" :
                    grille[i+100] = "electricitep3"
                if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                    grille[i-1] = "electricitem4"
                elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                    grille[i-1] = "electricitep4"
                grille[i] = "pile2"
            else :
                grille[i] = grille[i][0:4]+str(int(grille[i][4])-1)
                if grille[i][4] == "0" :
                    grille[i] = "pile3"

        elif len(grille[i]) == 5 and grille[i][0:4] == "cair" :
            if grille[i][4] == "0" :
                if i > 99 and grille[i-100] == "rien" or i-(i//100)*100 < 99 and grille[i+1] == "rien" or i < 5900 and grille[i+100] == "rien" or i-(i//100)*100 > 0 and grille[i-1] == "rien" :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "cair3"
            elif not grille[i][4] == "0" :
                grille[i] = grille[i][0:4]+str(int(grille[i][4])-1)

        elif len(grille[i]) == 5 and grille[i][0:4] == "cgaz" :
            if grille[i][4] == "0" :
                if i > 99 and (grille[i-100] == "vapeur" or grille[i-100] == "gaz") or i-(i//100)*100 < 99 and (grille[i+1] == "vapeur" or grille[i+1] == "gaz") or i < 5900 and (grille[i+100] == "vapeur" or grille[i+100] == "gaz") or i-(i//100)*100 > 0 and (grille[i-1] == "vapeur" or grille[i-1] == "gaz") :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "cgaz3"
            elif not grille[i][4] == "0" :
                grille[i] = grille[i][0:4]+str(int(grille[i][4])-1)

        elif len(grille[i]) == 5 and grille[i][0:4] == "chum" :
            if grille[i][4] == "0" :
                if i > 99 and (len(grille[i-100]) >= 4 and grille[i-100][0:3] == "hum" or len(grille[i-100]) == 7 and grille[i-100][0:5] == "perso") or i-(i//100)*100 < 99 and (len(grille[i+1]) >= 4 and grille[i+1][0:3] == "hum" or len(grille[i+1]) == 7 and grille[i+1][0:5] == "perso") or i < 5900 and (len(grille[i+100]) >= 4 and grille[i+100][0:3] == "hum" or len(grille[i+100]) == 7 and grille[i+100][0:5] == "perso") or i-(i//100)*100 > 0 and (len(grille[i-1]) >= 4 and grille[i-1][0:3] == "hum" or len(grille[i-1]) == 7 and grille[i-1][0:5] == "perso") :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "chum3"
            elif not grille[i][4] == "0" :
                grille[i] = grille[i][0:4]+str(int(grille[i][4])-1)

        elif len(grille[i]) == 9 and grille[i][0:8] == "cliquide" :
            if grille[i][8] == "0" :
                if i > 99 and (grille[i-100] == "eau" or grille[i-100] == "eau_toxique" or grille[i-100] == "poison" or grille[i-100] == "lave" or grille[i-100] == "petrolee" or grille[i-100] == "petrolea") or i-(i//100)*100 < 99 and (grille[i+1] == "eau" or grille[i+1] == "eau_toxique" or grille[i+1] == "poison" or grille[i+1] == "lave" or grille[i+1] == "petrolee" or grille[i+1] == "petrolea") or i < 5900 and (grille[i+100] == "eau" or grille[i+100] == "eau_toxique" or grille[i+100] == "poison" or grille[i+100] == "lave" or grille[i+100] == "petrolee" or grille[i+100] == "petrolea") or i-(i//100)*100 > 0 and (grille[i-1] == "eau" or grille[i-1] == "eau_toxique" or grille[i-1] == "poison" or grille[i-1] == "lave" or grille[i-1] == "petrolee" or grille[i-1] == "petrolea") :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "cliquide3"
            elif not grille[i][8] == "0" :
                grille[i] = grille[i][0:8]+str(int(grille[i][8])-1)

        elif len(grille[i]) >= 8 and grille[i][0:5] == "porte" :
            if grille[i][5] == "0" :
                if grille[i][6] == "1" :
                    for j in range (1,int(grille[i][7:len(grille[i])])+1) :
                        grille[i-100*j] = "porte"
                elif grille[i][6] == "2" :
                    for j in range (1,int(grille[i][7:len(grille[i])])+1) :
                        grille[i+j] = "porte"
                elif grille[i][6] == "3" :
                    for j in range (1,int(grille[i][7:len(grille[i])])+1) :
                        grille[i+100*j] = "porte"
                elif grille[i][6] == "4" :
                    for j in range (1,int(grille[i][7:len(grille[i])])+1) :
                        grille[i-j] = "porte"
            else :
                grille[i] = grille[i][0:5]+str(int(grille[i][5])-1)+grille[i][6:len(grille[i])]

        elif len(grille[i]) == 5 and grille[i][0:3] == "hum" :
            non = 0
            if not grille[i-100][0:3] == "hum" or not grille[i-200][0:3] == "hum" or not grille[i-300][0:3] == "hum" or not grille[i-400][0:3] == "hum" or not grille[i-500][0:3] == "hum" :
                non = 1
            if non == 0 :
                if grille[i][4] == "1" :
                    if not grille[i-99][0:3] == "hum" or not grille[i-199][0:3] == "hum" or not grille[i-299][0:3] == "hum" or not grille[i-399][0:3] == "hum" or not grille[i-499][0:3] == "hum" :
                        non = 1
                elif grille[i][4] == "2" :
                    if not grille[i-101][0:3] == "hum" or not grille[i-201][0:3] == "hum" or not grille[i-301][0:3] == "hum" or not grille[i-401][0:3] == "hum" or not grille[i-501][0:3] == "hum" :
                        non = 1
            if non == 1 :
                grille[i] = grille[i][0:4]

        elif grille[i] == "vide" :
            if i > 99 :
                if i-(i//100)*100 > 0 and not grille[i-101] == "vide" :
                    grille[i-101] = "rien"
                if not grille[i-100] == "vide" :
                    grille[i-100] = "rien"
                if i-(i//100)*100 < 99 and not grille[i-99] == "vide" :
                    grille[i-99] = "rien"
            if i-(i//100)*100 > 0 and not grille[i-1] == "vide" :
                grille[i-1] = "rien"
            if i-(i//100)*100 < 99 and not grille[i+1] == "vide" :
                grille[i+1] = "rien"
            if i < 5900 :
                if i-(i//100)*100 > 0 and not grille[i+99] == "vide" :
                    grille[i+99] = "rien"
                if not grille[i+100] == "vide" :
                    grille[i+100] = "rien"
                if i-(i//100)*100 < 99 and not grille[i+101] == "vide" :
                    grille[i+101] = "rien"

    for i in range (len(grille)) :
        if grille[i] == "laser" :
            for j in range (4) :
                if j == 0 :
                    direc = -100
                elif j == 1 :
                    direc = 1
                elif j == 2 :
                    direc = 100
                elif j == 3 :
                    direc = -1
                k = i
                etat = "0"
                if (i > 199 and j == 0 or i < 5800 and j == 2 or i-(i//100)*100 > 1 and j == 3 or i-(i//100)*100 < 98 and j == 1) and grille[i+direc] == "verre" :
                    k += direc*2
                    non = 0
                    non2 = 0
                    a = 0
                    while non == 0 :
                        if grille[k] == "rien" :
                            grille[k] = "laser"+etat
                        elif len(grille[k]) == 14 and grille[k][0:12] == "pelectricite" :
                            etat = "1"
                        elif len(grille[k]) == 12 and grille[k][0:10] == "pexplosion" :
                            etat = "2"
                            if grille[k][10] == "0" or grille[k][10] == "9" :
                                a = 1
                            else :
                                a = 0
                        elif len(grille[k]) == 6 and grille[k][0:4] == "pfeu" :
                            etat = "3"
                        elif len(grille[k]) == 8 and grille[k][0:6] == "pglace" :
                            etat = "4"
                        elif direc == -100 and grille[k] == "verre" and k-(k//100)*100 > 0 and grille[k+99] == "verre" and (k-(k//100)*100 == 99 or not grille[k+101] == "verre") :
                            direc = 1
                            k += 100
                        elif direc == -100 and grille[k] == "verre" and k-(k//100)*100 < 99 and grille[k+101] == "verre" and (k-(k//100)*100 == 0 or not grille[k+99] == "verre") :
                            direc = -1
                            k += 100
                        elif direc == 1 and grille[k] == "verre" and k < 5900 and grille[k+99] == "verre" and (k < 100 or not grille[k-101] == "verre") :
                            direc = -100
                            k -= 1
                        elif direc == 1 and grille[k] == "verre" and k > 99 and grille[k-101] == "verre" and (k > 5899 or not grille[k+99] == "verre") :
                            direc = 100
                            k -= 1
                        elif direc == 100 and grille[k] == "verre" and k-(k//100)*100 > 0 and grille[k-101] == "verre" and (k-(k//100)*100 == 99 or not grille[k-99] == "verre") :
                            direc = 1
                            k -= 100
                        elif direc == 100 and grille[k] == "verre" and k-(k//100)*100 < 99 and grille[k-99] == "verre" and (k-(k//100)*100 == 0 or not grille[k-101] == "verre") :
                            direc = -1
                            k -= 100
                        elif direc == -1 and grille[k] == "verre" and k < 5900 and grille[k+101] == "verre" and (k < 100 or not grille[k-99] == "verre") :
                            direc = -100
                            k += 1
                        elif direc == -1 and grille[k] == "verre" and k > 99 and grille[k-99] == "verre" and (k > 5899 or not grille[k+101] == "verre") :
                            direc = 100
                            k += 1
                        elif grille[k] == "verre" or grille[k][0:3] == "feu" or len(grille[k]) == 6 and grille[k][0:5] == "laser" or (grille[i] == "eau" or grille[i] == "eau_toxique") and not etat == "3" and not etat == "4" or grille[i] == "vapeur" and not etat == "4" or grille[i] == "gaz" and not etat == "3" :
                            non2 = 0
                            elt = grille[k]
                            while non2 == 0 :
                                if (k > -1 and direc == -100 or k < 6000 and direc == 100 or k-(k//100)*100 >= 0 and direc == -1 or k-(k//100)*100 <= 99 and direc == 1) and grille[k] == elt :
                                    k += direc
                                else :
                                    non2 = 1
                            k -= direc
                        else :
                            non = 1
                        if k > 99 and direc == -100 or k < 5900 and direc == 100 or k-(k//100)*100 > 0 and direc == -1 or k-(k//100)*100 < 99 and direc == 1 :
                            k += direc
                        else :
                            non = 1
                    if etat == "1" and (k > 99 and direc == -100 or k < 5900 and direc == 100 or k-(k//100)*100 > 0 and direc == 1 or k-(k//100)*100 < 99 and direc == -1) :
                        if grille[k-direc] == "metal" :
                            if direc == -100 :
                                grille[k-direc] = "electricitem1"
                            if direc == 1 :
                                grille[k-direc] = "electricitem2"
                            if direc == 100 :
                                grille[k-direc] = "electricitem3"
                            if direc == -1 :
                                grille[k-direc] = "electricitem4"
                        elif grille[k-direc] == "pont" :
                            if direc == -100 :
                                grille[k-direc] = "electricitep1"
                            if direc == 1 :
                                grille[k-direc] = "electricitep2"
                            if direc == 100 :
                                grille[k-direc] = "electricitep3"
                            if direc == -1 :
                                grille[k-direc] = "electricitep4"
                    elif a == 1 and etat == "2" :
                        grille[k] = "feu2"
                        if k > 299 :
                            grille[k-300] = "feu2"
                        if k > 199 :
                            grille[k-200] = "feu2"
                        if k > 99 :
                            grille[k-100] = "feu2"
                        if k-(k//100)*100 < 97 :
                            grille[k+3] = "feu2"
                        if k-(k//100)*100 < 98 :
                            grille[k+2] = "feu2"
                        if k-(k//100)*100 < 99 :
                            grille[k+1] = "feu2"
                        if k < 5700 :
                            grille[k+300] = "feu2"
                        if k < 5800 :
                            grille[k+200] = "feu2"
                        if k < 5900 :
                            grille[k+100] = "feu2"
                        if k-(k//100)*100 > 2 :
                            grille[k-3] = "feu2"
                        if k-(k//100)*100 > 1 :
                            grille[k-2] = "feu2"
                        if k-(k//100)*100 > 0 :
                            grille[k-1] = "feu2"
                        if k > 99 and k-(k//100)*100 > 0 :
                            grille[k-101] = "feu2"
                        if k > 99 and k-(k//100)*100 < 99 :
                            grille[k-99] = "feu2"
                        if k < 5900 and k-(k//100)*100 > 0 :
                            grille[k+99] = "feu2"
                        if k < 5900 and k-(k//100)*100 < 99 :
                            grille[k+101] = "feu2"
                        if k > 99 and k-(k//100)*100 > 1 :
                            grille[k-102] = "feu2"
                        if k > 199 and k-(k//100)*100 > 0 :
                            grille[k-201] = "feu2"
                        if k > 199 and k-(k//100)*100 < 99 :
                            grille[k-199] = "feu2"
                        if k > 99 and k-(k//100)*100 < 98 :
                            grille[k-98] = "feu2"
                        if k < 5900 and k-(k//100)*100 < 98 :
                            grille[k+102] = "feu2"
                        if k < 5800 and k-(k//100)*100 < 99 :
                            grille[k+201] = "feu2"
                        if k < 5800 and k-(k//100)*100 > 0 :
                            grille[k+199] = "feu2"
                        if k < 5900 and k-(k//100)*100 > 1 :
                            grille[k+98] = "feu2"
                    elif etat == "3" :
                        temperature[k] += 4
                        if k > 299 :
                            temperature[k-300] += 1
                        if k > 199 :
                            temperature[k-200] += 2
                        if k > 99 :
                            temperature[k-100] += 3
                        if k-(k//100)*100 < 97 :
                            temperature[k+3] += 1
                        if k-(k//100)*100 < 98 :
                            temperature[k+2] += 2
                        if k-(k//100)*100 < 99 :
                            temperature[k+1] += 3
                        if k < 5700 :
                            temperature[k+300] += 1
                        if k < 5800 :
                            temperature[k+200] += 2
                        if k < 5900 :
                            temperature[k+100] += 3
                        if k-(k//100)*100 > 2 :
                            temperature[k-3] += 1
                        if k-(k//100)*100 > 1 :
                            temperature[k-2] += 2
                        if k-(k//100)*100 > 0 :
                            temperature[k-1] += 3
                        if k > 99 and k-(k//100)*100 > 0 :
                            temperature[k-101] += 2
                        if k > 99 and k-(k//100)*100 < 99 :
                            temperature[k-99] += 2
                        if k < 5900 and k-(k//100)*100 > 0 :
                            temperature[k+99] += 2
                        if k < 5900 and k-(k//100)*100 < 99 :
                            temperature[k+101] += 2
                        if k > 99 and k-(k//100)*100 > 1 :
                            temperature[k-102] += 1
                        if k > 199 and k-(k//100)*100 > 0 :
                            temperature[k-201] += 1
                        if k > 199 and k-(k//100)*100 < 99 :
                            temperature[k-199] += 1
                        if k > 99 and k-(k//100)*100 < 98 :
                            temperature[k-98] += 1
                        if k < 5900 and k-(k//100)*100 < 98 :
                            temperature[k+102] += 1
                        if k < 5800 and k-(k//100)*100 < 99 :
                            temperature[k+201] += 1
                        if k < 5800 and k-(k//100)*100 > 0 :
                            temperature[k+199] += 1
                        if k < 5900 and k-(k//100)*100 > 1 :
                            temperature[k+98] += 1
                    elif etat == "4" :
                        temperature[k] -= 4
                        if k > 299 :
                            temperature[k-300] -= 1
                        if k > 199 :
                            temperature[k-200] -= 2
                        if k > 99 :
                            temperature[k-100] -= 3
                        if k-(k//100)*100 < 97 :
                            temperature[k+3] -= 1
                        if k-(k//100)*100 < 98 :
                            temperature[k+2] -= 2
                        if k-(k//100)*100 < 99 :
                            temperature[k+1] -= 3
                        if k < 5700 :
                            temperature[k+300] -= 1
                        if k < 5800 :
                            temperature[k+200] -= 2
                        if k < 5900 :
                            temperature[k+100] -= 3
                        if k-(k//100)*100 > 2 :
                            temperature[k-3] -= 1
                        if k-(k//100)*100 > 1 :
                            temperature[k-2] -= 2
                        if k-(k//100)*100 > 0 :
                            temperature[k-1] -= 3
                        if k > 99 and k-(k//100)*100 > 0 :
                            temperature[k-101] -= 2
                        if k > 99 and k-(k//100)*100 < 99 :
                            temperature[k-99] -= 2
                        if k < 5900 and k-(k//100)*100 > 0 :
                            temperature[k+99] -= 2
                        if k < 5900 and k-(k//100)*100 < 99 :
                            temperature[k+101] -= 2
                        if k > 99 and k-(k//100)*100 > 1 :
                            temperature[k-102] -= 1
                        if k > 199 and k-(k//100)*100 > 0 :
                            temperature[k-201] -= 1
                        if k > 199 and k-(k//100)*100 < 99 :
                            temperature[k-199] -= 1
                        if k > 99 and k-(k//100)*100 < 98 :
                            temperature[k-98] -= 1
                        if k < 5900 and k-(k//100)*100 < 98 :
                            temperature[k+102] -= 1
                        if k < 5800 and k-(k//100)*100 < 99 :
                            temperature[k+201] -= 1
                        if k < 5800 and k-(k//100)*100 > 0 :
                            temperature[k+199] -= 1
                        if k < 5900 and k-(k//100)*100 > 1 :
                            temperature[k+98] -= 1

    for i in range (len(grille)) :
        if grille[i] == "gaz" :
            direc = randint(1,4)
            if direc == 1 and i > 99 and grille[i-100] == "rien" :
                grille[i-100] = "gaz0"
                grille[i] = "rien"
            elif direc == 2 and i-(i//100)*100 < 99 and grille[i+1] == "rien" :
                grille[i+1] = "gaz0"
                grille[i] = "rien"
            elif direc == 3 and i < 5900 and grille[i+100] == "rien" :
                grille[i+100] = "gaz0"
                grille[i] = "rien"
            elif direc == 4 and i-(i//100)*100 > 0 and grille[i-1] == "rien" :
                grille[i-1] = "gaz0"
                grille[i] = "rien"

    for i in range (len(grille)) :
        if grille[i] == "gaz0" :
            grille[i] = "gaz"

    for i in range (len(temperature)) :
        if grille[i][0:3] == "feu" or len(grille[i]) >= 8 and grille[i][0:8] == "petrolea" :
            if i > 199 :
                temperature[i-200] += 1
            if i > 99 :
                temperature[i-100] += 2
            if i-(i//100)*100 < 98 :
                temperature[i+2] += 1
            if i-(i//100)*100 < 99 :
                temperature[i+1] += 2
            if i < 5800 :
                temperature[i+200] += 1
            if i < 5900 :
                temperature[i+100] += 2
            if i-(i//100)*100 > 1 :
                temperature[i-2] += 1
            if i-(i//100)*100 > 0 :
                temperature[i-1] += 2
            if i > 99 and i-(i//100)*100 > 0 :
                temperature[i-101] += 1
            if i > 99 and i-(i//100)*100 < 99 :
                temperature[i-99] += 1
            if i < 5900 and i-(i//100)*100 > 0 :
                temperature[i+99] += 1
            if i < 5900 and i-(i//100)*100 < 99 :
                temperature[i+101] += 1

        elif grille[i] == "lave" or len(grille[i]) == 11 and grille[i][0:10] == "radiateuro" :
            if i > 299 :
                temperature[i-300] += 1
            if i > 199 :
                temperature[i-200] += 2
            if i > 99 :
                temperature[i-100] += 3
            if i-(i//100)*100 < 97 :
                temperature[i+3] += 1
            if i-(i//100)*100 < 98 :
                temperature[i+2] += 2
            if i-(i//100)*100 < 99 :
                temperature[i+1] += 3
            if i < 5700 :
                temperature[i+300] += 1
            if i < 5800 :
                temperature[i+200] += 2
            if i < 5900 :
                temperature[i+100] += 3
            if i-(i//100)*100 > 2 :
                temperature[i-3] += 1
            if i-(i//100)*100 > 1 :
                temperature[i-2] += 2
            if i-(i//100)*100 > 0 :
                temperature[i-1] += 3
            if i > 99 and i-(i//100)*100 > 0 :
                temperature[i-101] += 2
            if i > 99 and i-(i//100)*100 < 99 :
                temperature[i-99] += 2
            if i < 5900 and i-(i//100)*100 > 0 :
                temperature[i+99] += 2
            if i < 5900 and i-(i//100)*100 < 99 :
                temperature[i+101] += 2
            if i > 99 and i-(i//100)*100 > 1 :
                temperature[i-102] += 1
            if i > 199 and i-(i//100)*100 > 0 :
                temperature[i-201] += 1
            if i > 199 and i-(i//100)*100 < 99 :
                temperature[i-199] += 1
            if i > 99 and i-(i//100)*100 < 98 :
                temperature[i-98] += 1
            if i < 5900 and i-(i//100)*100 < 98 :
                temperature[i+102] += 1
            if i < 5800 and i-(i//100)*100 < 99 :
                temperature[i+201] += 1
            if i < 5800 and i-(i//100)*100 > 0 :
                temperature[i+199] += 1
            if i < 5900 and i-(i//100)*100 > 1 :
                temperature[i+98] += 1

        elif grille[i] == "glace" or len(grille[i]) == 15 and grille[i][0:14] == "refrigirateuro" :
            if i > 299 :
                temperature[i-300] -= 1
            if i > 199 :
                temperature[i-200] -= 2
            if i > 99 :
                temperature[i-100] -= 3
            if i-(i//100)*100 < 97 :
                temperature[i+3] -= 1
            if i-(i//100)*100 < 98 :
                temperature[i+2] -= 2
            if i-(i//100)*100 < 99 :
                temperature[i+1] -= 3
            if i < 5700 :
                temperature[i+300] -= 1
            if i < 5800 :
                temperature[i+200] -= 2
            if i < 5900 :
                temperature[i+100] -= 3
            if i-(i//100)*100 > 2 :
                temperature[i-3] -= 1
            if i-(i//100)*100 > 1 :
                temperature[i-2] -= 2
            if i-(i//100)*100 > 0 :
                temperature[i-1] -= 3
            if i > 99 and i-(i//100)*100 > 0 :
                temperature[i-101] -= 2
            if i > 99 and i-(i//100)*100 < 99 :
                temperature[i-99] -= 2
            if i < 5900 and i-(i//100)*100 > 0 :
                temperature[i+99] -= 2
            if i < 5900 and i-(i//100)*100 < 99 :
                temperature[i+101] -= 2
            if i > 99 and i-(i//100)*100 > 1 :
                temperature[i-102] -= 1
            if i > 199 and i-(i//100)*100 > 0 :
                temperature[i-201] -= 1
            if i > 199 and i-(i//100)*100 < 99 :
                temperature[i-199] -= 1
            if i > 99 and i-(i//100)*100 < 98 :
                temperature[i-98] -= 1
            if i < 5900 and i-(i//100)*100 < 98 :
                temperature[i+102] -= 1
            if i < 5800 and i-(i//100)*100 < 99 :
                temperature[i+201] -= 1
            if i < 5800 and i-(i//100)*100 > 0 :
                temperature[i+199] -= 1
            if i < 5900 and i-(i//100)*100 > 1 :
                temperature[i+98] -= 1

    for i in range (len(grille)) :
        if len(grille[i]) == 9 and grille[i][0:8] == "cchaleur" :
            if grille[i][8] == "0" :
                t = 0
                if temperature[i] >= 8 :
                    t = "0"
                elif temperature[i] >= 6 :
                    t = "1"
                elif temperature[i] >= 4 :
                    t = "2"
                elif temperature[i] >= 2 :
                    t = "3"
                if not t == 0 :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "cchaleur"+t
            elif not grille[i][8] == "0" :
                grille[i] = grille[i][0:8]+str(int(grille[i][8])-1)

        elif len(grille[i]) == 7 and grille[i][0:6] == "cfroid" :
            if grille[i][6] == "0" :
                t = 0
                if temperature[i] <= -8 :
                    t = "0"
                elif temperature[i] <= -6 :
                    t = "1"
                elif temperature[i] <= -4 :
                    t = "2"
                elif temperature[i] <= -2 :
                    t = "3"
                if not t == 0 :
                    if i > 99 and grille[i-100] == "metal" :
                        grille[i-100] = "electricitem1"
                    elif i > 99 and grille[i-100] == "pont" :
                        grille[i-100] = "electricitep1"
                    if i-(i//100)*100 < 99 and grille[i+1] == "metal" :
                        grille[i+1] = "electricitem2"
                    elif i-(i//100)*100 < 99 and grille[i+1] == "pont" :
                        grille[i+1] = "electricitep2"
                    if i < 5900 and grille[i+100] == "metal" :
                        grille[i+100] = "electricitem3"
                    elif i < 5900 and grille[i+100] == "pont" :
                        grille[i+100] = "electricitep3"
                    if i-(i//100)*100 > 0 and grille[i-1] == "metal" :
                        grille[i-1] = "electricitem4"
                    elif i-(i//100)*100 > 0 and grille[i-1] == "pont" :
                        grille[i-1] = "electricitep4"
                    grille[i] = "cfroid"+t
            elif not grille[i][6] == "0" :
                grille[i] = grille[i][0:6]+str(int(grille[i][6])-1)
        elif (len(grille[i]) >= 4 and grille[i][0:4] == "bois" or len(grille[i]) >= 8 and grille[i][0:8] == "ffeuille") and temperature[i] > 2 :
            grille[i] = "feu2"
        elif (len(grille[i]) == 5 and grille[i][0:3] == "hum" or len(grille[i]) == 7 and grille[i][0:5] == "perso") and temperature[i] > 2 :
            if len(grille[i]) == 5 and grille[i][4] == "1" or len(grille[i]) == 7 and grille[i][5] == "1" :
                for j in range (6) :
                    grille[(i+1)-j*100] = "feu2"
            elif len(grille[i]) == 5 and grille[i][4] == "2" or len(grille[i]) == 7 and grille[i][5] == "2" :
                for j in range (6) :
                    grille[(i-1)-j*100] = "feu2"
            for j in range (6) :
                grille[i-j*100] = "feu2"
        elif grille[i] == "gaz" and temperature[i] > 0 :
            grille[i] = "feu2"
        elif grille[i] == "lave" and temperature[i] < 0 :
            grille[i] = "pierre"
        elif grille[i] == "petrolee" and temperature[i] > 2 :
            grille[i] = "petrolea6"
        elif grille[i] == "pierre" and temperature[i] > 4 :
            grille[i] = "lave"
        elif grille[i] == "sable" and temperature[i] > 3 :
            grille[i] = "verre"
        elif grille[i] == "tnt" and temperature[i] > 3 :
            grille[i] = "feu2"
            if i > 299 :
                grille[i-300] = "feu2"
            if i > 199 :
                grille[i-200] = "feu2"
            if i > 99 :
                grille[i-100] = "feu2"
            if i-(i//100)*100 < 97 :
                grille[i+3] = "feu2"
            if i-(i//100)*100 < 98 :
                grille[i+2] = "feu2"
            if i-(i//100)*100 < 99 :
                grille[i+1] = "feu2"
            if i < 5700 :
                grille[i+300] = "feu2"
            if i < 5800 :
                grille[i+200] = "feu2"
            if i < 5900 :
                grille[i+100] = "feu2"
            if i-(i//100)*100 > 2 :
                grille[i-3] = "feu2"
            if i-(i//100)*100 > 1 :
                grille[i-2] = "feu2"
            if i-(i//100)*100 > 0 :
                grille[i-1] = "feu2"
            if i > 99 and i-(i//100)*100 > 0 :
                grille[i-101] = "feu2"
            if i > 99 and i-(i//100)*100 < 99 :
                grille[i-99] = "feu2"
            if i < 5900 and i-(i//100)*100 > 0 :
                grille[i+99] = "feu2"
            if i < 5900 and i-(i//100)*100 < 99 :
                grille[i+101] = "feu2"
            if i > 99 and i-(i//100)*100 > 1 :
                grille[i-102] = "feu2"
            if i > 199 and i-(i//100)*100 > 0 :
                grille[i-201] = "feu2"
            if i > 199 and i-(i//100)*100 < 99 :
                grille[i-199] = "feu2"
            if i > 99 and i-(i//100)*100 < 98 :
                grille[i-98] = "feu2"
            if i < 5900 and i-(i//100)*100 < 98 :
                grille[i+102] = "feu2"
            if i < 5800 and i-(i//100)*100 < 99 :
                grille[i+201] = "feu2"
            if i < 5800 and i-(i//100)*100 > 0 :
                grille[i+199] = "feu2"
            if i < 5900 and i-(i//100)*100 > 1 :
                grille[i+98] = "feu2"
        elif grille[i] == "glace" and temperature[i] > 0 :
            grille[i] = "eau"
        elif grille[i] == "eau" and temperature[i] < -1 :
            grille[i] = "glace"
        elif (grille[i] == "eau" or grille[i] == "eau_toxique") and temperature[i] > 1 :
            grille[i] = "vapeur"
        elif grille[i] == "vapeur" and temperature[i] < 0 :
            grille[i] = "eau"

        if i < 5800 and grille[i] == "poison" :
            if grille[i+100] == "eau" and not grille[i+200] == "rien" and not grille[i+200][0:3] == "feu" :
                grille[i+100] = "eau_toxique"
                grille[i] = "rien"
        if i < 5900 and i >= 5800 and grille[i] == "poison" :
            if grille[i+100] == "eau" :
                grille[i+100] = "eau_toxique"
                grille[i] = "rien"

        if i < 5800 and grille[i] == "eau" :
            if grille[i+100] == "poison" and not grille[i+200] == "rien" and not grille[i+200][0:3] == "feu" :
                grille[i+100] = "eau_toxique"
                grille[i] = "rien"
        if i < 5900 and i >= 5800 and grille[i] == "eau" :
            if grille[i+100] == "poison" :
                grille[i+100] = "eau_toxique"
                grille[i] = "rien"
        if i >= 5900 and grille[i] == "eau" :
            if i-(i//100)*100 > 0 and grille[i-1] == "poison" :
                grille[i-1] = "rien"
                grille[i] = "eau_toxique"
            if i-(i//100)*100 < 99 and grille[i+1] == "poison" :
                grille[i+1] = "rien"
                grille[i] = "eau_toxique"
        if i < 5900 and not grille[i+100] == "rien" and grille[i] == "eau" :
            if i-(i//100)*100 > 0 and grille[i-1] == "poison" and not grille[i+99] == "rien" and not grille[i+99][0:3] == "feu" :
                grille[i-1] = "rien"
                grille[i] = "eau_toxique"
            if i-(i//100)*100 < 99 and grille[i+1] == "poison" and not grille[i+101] == "rien" and not grille[i+101][0:3] == "feu" :
                grille[i+1] = "rien"
                grille[i] = "eau_toxique"

    affichage()

def affichage() :
    global ecran
    global grille
    global pause
    global nom
    global son
    if ecran == 0 :
        fenetre.blit(menu,(0,0))
    elif ecran == 1 or ecran == 3 or ecran == 4 or ecran == 5 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,1000,50))
        pygame.draw.rect(fenetre,(85,85,85),(0,50,1000,650))
        fenetre.blit(crayon,(5,5))
        fenetre.blit(gomme,(55,5))
        fenetre.blit(croix,(105,5))
        pygame.draw.line(fenetre,(106,106,106),(155,0),(155,50))
        fenetre.blit(bouton_sauvegarder,(160,5))
        fenetre.blit(bouton_ouvrir,(210,5))
        pygame.draw.line(fenetre,(106,106,106),(255,0),(255,50))
        if son == 1 :
            fenetre.blit(bouton_son_on,(265,5))
        else :
            fenetre.blit(bouton_son_off,(265,5))
        if pause == 0 :
            fenetre.blit(bouton_pause,(480,5))
        else :
            fenetre.blit(play,(480,5))
        fenetre.blit(bouton_elements,(955,5))
        for i in range (60) :
            for j in range (100) :
                if grille[i*100+j] == "beton" :
                    pygame.draw.rect(fenetre,(185,122,87),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "bdirigeable" :
                    pygame.draw.rect(fenetre,(0,128,128),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) >= 4 and grille[i*100+j][0:4] == "bois" :
                    pygame.draw.rect(fenetre,(85,0,13),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "boue" :
                    pygame.draw.rect(fenetre,(85,43,0),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 5 and grille[i*100+j][0:4] == "cair" :
                    pygame.draw.rect(fenetre,(145,186,20),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 9 and grille[i*100+j][0:8] == "cchaleur" :
                    pygame.draw.rect(fenetre,(244,80,0),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 7 and grille[i*100+j][0:6] == "cfroid" :
                    pygame.draw.rect(fenetre,(112,146,190),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 5 and grille[i*100+j][0:4] == "cgaz" :
                    pygame.draw.rect(fenetre,(163,73,164),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 5 and grille[i*100+j][0:4] == "chum" :
                    pygame.draw.rect(fenetre,(130,220,170),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 9 and grille[i*100+j][0:8] == "cliquide" :
                    pygame.draw.rect(fenetre,(63,72,204),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "eau" :
                    pygame.draw.rect(fenetre,(0,162,232),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "eau_toxique" :
                    pygame.draw.rect(fenetre,(90,196,131),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 13 and grille[i*100+j][0:11] == "electricite" :
                    pygame.draw.rect(fenetre,(255,242,0),(j*10,i*10+50,10,10))
                elif grille[i*100+j][0:3] == "feu" :
                    pygame.draw.rect(fenetre,(253,150,11),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) >= 8 and grille[i*100+j][0:8] == "ffeuille" :
                    pygame.draw.rect(fenetre,(22,116,50),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "gaz" :
                    pygame.draw.rect(fenetre,(250,250,200),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "glace" :
                    pygame.draw.rect(fenetre,(153,217,234),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "graine" :
                    pygame.draw.rect(fenetre,(0,255,64),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "hum" or grille[i*100+j] == "perso" :
                    pygame.draw.rect(fenetre,(200,200,100),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) >= 4 and grille[i*100+j][0:3] == "hum" :
                    pygame.draw.rect(fenetre,couleurs_hum[int(grille[i*100+j][3])-1],(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 7 and grille[i*100+j][0:5] == "lampe" :
                    if grille[i*100+j][5] == "o" :
                        pygame.draw.rect(fenetre,(255,201,14),(j*10,i*10+50,10,10))
                    else :
                        pygame.draw.rect(fenetre,(106,83,0),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "laser" :
                    pygame.draw.rect(fenetre,(128,64,64),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:5] == "laser" and grille[i*100+j][5] == "0" :
                    pygame.draw.rect(fenetre,(230,230,230),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:5] == "laser" and grille[i*100+j][5] == "1" :
                    pygame.draw.rect(fenetre,(255,255,100),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:5] == "laser" and grille[i*100+j][5] == "2" :
                    pygame.draw.rect(fenetre,(255,150,100),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:5] == "laser" and grille[i*100+j][5] == "3" :
                    pygame.draw.rect(fenetre,(255,100,100),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:5] == "laser" and grille[i*100+j][5] == "4" :
                    pygame.draw.rect(fenetre,(220,200,255),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "lave" :
                    pygame.draw.rect(fenetre,(255,127,39),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "metal" :
                    pygame.draw.rect(fenetre,(195,195,195),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) >= 5 and grille[i*100+j][0:5] == "multi" :
                    pygame.draw.rect(fenetre,(255,0,128),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 7 and grille[i*100+j][0:5] == "perso" :
                    pygame.draw.rect(fenetre,(142,88,60),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "petrolee" :
                    pygame.draw.rect(fenetre,(53,53,53),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 9 and grille[i*100+j][0:8] == "petrolea" :
                    pygame.draw.rect(fenetre,(153,53,53),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "pierre" :
                    pygame.draw.rect(fenetre,(127,127,127),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 14 and grille[i*100+j][0:12] == "pelectricite" :
                    pygame.draw.rect(fenetre,(250-int(grille[i*100+j][12])*10,250-int(grille[i*100+j][12]),0),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 12 and grille[i*100+j][0:10] == "pexplosion" :
                    pygame.draw.rect(fenetre,(255,100+int(grille[i*100+j][10]),0+int(grille[i*100+j][10])*10),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 6 and grille[i*100+j][0:4] == "pfeu" :
                    pygame.draw.rect(fenetre,(255,0+int(grille[i*100+j][4]),0+int(grille[i*100+j][4])*10),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 8 and grille[i*100+j][0:6] == "pglace" :
                    pygame.draw.rect(fenetre,(55+int(grille[i*100+j][6])*10,155+int(grille[i*100+j][6]),255),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 5 and grille[i*100+j][0:4] == "pile" :
                    pygame.draw.rect(fenetre,(0,0,128),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "poison" :
                    pygame.draw.rect(fenetre,(181,230,29),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "pont" :
                    pygame.draw.rect(fenetre,(160,15,35),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) >= 8 and grille[i*100+j][0:5] == "porte" :
                    pygame.draw.rect(fenetre,(181,147,147),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "porte" :
                    pygame.draw.rect(fenetre,(200,180,180),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 11 and grille[i*100+j][0:9] == "radiateur" :
                    pygame.draw.rect(fenetre,(243,29,50),(j*10,i*10+50,10,10))
                elif len(grille[i*100+j]) == 15 and grille[i*100+j][0:13] == "refrigirateur" :
                    pygame.draw.rect(fenetre,(20,90,100),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "sable" :
                    pygame.draw.rect(fenetre,(239,228,176),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "terre" :
                    pygame.draw.rect(fenetre,(128,64,0),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "tnt" :
                    pygame.draw.rect(fenetre,(157,13,20),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "vapeur" :
                    pygame.draw.rect(fenetre,(200,191,231),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "verre" :
                    pygame.draw.rect(fenetre,(207,207,207),(j*10,i*10+50,10,10))
                elif grille[i*100+j] == "vide" :
                    pygame.draw.rect(fenetre,(0,0,0),(j*10,i*10+50,10,10))
        for i in range (60) :
            for j in range (100) :
                if temperature[i*100+j] < 0 :
                    rect = pygame.Surface((10,10))
                    rect.set_alpha(20*abs(temperature[i*100+j]))
                    if rect.get_alpha() > 100 :
                        rect.set_alpha(100)
                    rect.fill((180,230,240))
                    fenetre.blit(rect,(j*10,i*10+50))
                elif temperature[i*100+j] > 0 :
                    rect = pygame.Surface((10,10))
                    rect.set_alpha(20*temperature[i*100+j])
                    if rect.get_alpha() > 100 :
                        rect.set_alpha(100)
                    rect.fill((250,80,0))
                    fenetre.blit(rect,(j*10,i*10+50))

        if ecran == 5 :
            pygame.draw.rect(fenetre,(181,147,147),(ajout_porte[0]*10,ajout_porte[1]*10+50,10,10))
            if ajout_porte[2] == 1 :
                for i in range (1,ajout_porte[3]+1) :
                    pygame.draw.rect(fenetre,(200,180,180),(ajout_porte[0]*10,ajout_porte[1]*10+50-i*10,10,10))
            elif ajout_porte[2] == 2 :
                for i in range (1,ajout_porte[3]+1) :
                    pygame.draw.rect(fenetre,(200,180,180),(ajout_porte[0]*10+i*10,ajout_porte[1]*10+50,10,10))
            elif ajout_porte[2] == 3 :
                for i in range (1,ajout_porte[3]+1) :
                    pygame.draw.rect(fenetre,(200,180,180),(ajout_porte[0]*10,ajout_porte[1]*10+50+i*10,10,10))
            elif ajout_porte[2] == 4 :
                for i in range (1,ajout_porte[3]+1) :
                    pygame.draw.rect(fenetre,(200,180,180),(ajout_porte[0]*10-i*10,ajout_porte[1]*10+50,10,10))

    elif ecran == 2 :
        pygame.draw.rect(fenetre,(125,125,125),(0,0,1000,650))
        fenetre.blit(fleche,(5,5))

        fenetre.blit(bouton_beton,(7,55))
        fenetre.blit(bouton_bloc_dirigeable,(52,55))
        fenetre.blit(bouton_bois,(97,55))
        fenetre.blit(bouton_boue,(142,55))
        fenetre.blit(bouton_capteur_air,(187,55))
        fenetre.blit(bouton_capteur_chaleur,(232,55))
        fenetre.blit(bouton_capteur_froid,(277,55))
        fenetre.blit(bouton_capteur_gaz,(322,55))
        fenetre.blit(bouton_capteur_humain,(367,55))
        fenetre.blit(bouton_capteur_liquide,(412,55))
        fenetre.blit(bouton_eau,(457,55))
        fenetre.blit(bouton_electricite,(502,55))
        fenetre.blit(bouton_feu,(547,55))
        fenetre.blit(bouton_gaz,(592,55))
        fenetre.blit(bouton_glace,(637,55))
        fenetre.blit(bouton_graine,(682,55))
        fenetre.blit(bouton_humain,(727,55))
        fenetre.blit(bouton_lampe,(772,55))
        fenetre.blit(bouton_laser,(817,55))
        fenetre.blit(bouton_lave,(862,55))
        fenetre.blit(bouton_metal,(907,55))
        fenetre.blit(bouton_multi,(952,55))
        fenetre.blit(bouton_perso,(7,100))
        fenetre.blit(bouton_petrole,(52,100))
        fenetre.blit(bouton_pierre,(97,100))
        fenetre.blit(bouton_pierre_electricite,(142,100))
        fenetre.blit(bouton_pierre_explosion,(187,100))
        fenetre.blit(bouton_pierre_feu,(232,100))
        fenetre.blit(bouton_pierre_glace,(277,100))
        fenetre.blit(bouton_pile,(322,100))
        fenetre.blit(bouton_poison,(367,100))
        fenetre.blit(bouton_pont,(412,100))
        fenetre.blit(bouton_porte,(457,100))
        fenetre.blit(bouton_radiateur,(502,100))
        fenetre.blit(bouton_refrigirateur,(547,100))
        fenetre.blit(bouton_sable,(592,100))
        fenetre.blit(bouton_terre,(637,100))
        fenetre.blit(bouton_tnt,(682,100))
        fenetre.blit(bouton_vapeur,(727,100))
        fenetre.blit(bouton_verre,(772,100))
        fenetre.blit(bouton_vide,(817,100))

    if ecran == 3 or ecran == 4 :
        pygame.draw.rect(fenetre,(125,125,125),(390,280,220,65))
        pygame.draw.rect(fenetre,(0,0,0),(395,310,210,30))
        pygame.draw.rect(fenetre,(255,255,255),(398,313,204,24))
        myfont = pygame.font.SysFont("Courier",20)
        texte = myfont.render("Nom sauvegarde :",False,(0,0,0))
        fenetre.blit(texte,(400,285))
        texte = myfont.render(nom,False,(0,0,0))
        fenetre.blit(texte,(400,315))

    pygame.display.flip()

def sauvegarde() :
    global ecran
    global grille
    global nom
    if ecran == 3 :
        s = open(raccourci+"sauvegardes\\"+nom+".txt","w")
        texte = ""
        for i in range (len(grille)) :
            texte += grille[i]+"/"
        s.write(texte)
        s.close()
        ecran = 1
    elif ecran == 4 :
        if os.path.isfile(raccourci+"sauvegardes\\"+nom+".txt") :
            s = open(raccourci+"sauvegardes\\"+nom+".txt","r")
            texte = s.read()
            if not texte == "" :
                s.close()
                mot = ""
                grille = []
                for i in range (len(texte)) :
                    if texte[i] == "/" :
                        grille += [mot]
                        mot = ""
                    else :
                        mot += texte[i]
                ecran = 1

pygame.init()

raccourci = __file__
raccourci = raccourci[0:-8]

# fenêtre
fenetre = pygame.display.set_mode((1000,650))
pygame.display.set_caption("World Buider")

icone = pygame.image.load(raccourci+"sprite\\icone.png")
pygame.display.set_icon(icone)

# sprites
menu = pygame.image.load(raccourci+"sprite\\menu.png").convert()

crayon = pygame.image.load(raccourci+"sprite\\crayon.png").convert()
crayon.set_colorkey((255,255,255))
gomme = pygame.image.load(raccourci+"sprite\\gomme.png").convert()
gomme.set_colorkey((255,255,255))
croix = pygame.image.load(raccourci+"sprite\\croix.png").convert()
croix.set_colorkey((255,255,255))
bouton_sauvegarder = pygame.image.load(raccourci+"sprite\\bouton_sauvegarder.png").convert()
bouton_sauvegarder.set_colorkey((255,255,255))
bouton_ouvrir = pygame.image.load(raccourci+"sprite\\bouton_ouvrir.png").convert()
bouton_ouvrir.set_colorkey((255,255,255))
bouton_son_on = pygame.image.load(raccourci+"sprite\\bouton_son_on.png").convert()
bouton_son_on.set_colorkey((127,127,127))
bouton_son_off = pygame.image.load(raccourci+"sprite\\bouton_son_off.png").convert()
bouton_son_off.set_colorkey((127,127,127))
bouton_pause = pygame.image.load(raccourci+"sprite\\pause.png").convert()
bouton_pause.set_colorkey((127,127,127))
play = pygame.image.load(raccourci+"sprite\\play.png").convert()
play.set_colorkey((127,127,127))
bouton_elements = pygame.image.load(raccourci+"sprite\\bouton_elements.png").convert()
bouton_elements.set_colorkey((255,255,255))
fleche = pygame.image.load(raccourci+"sprite\\fleche.png").convert()
fleche.set_colorkey((127,127,127))

bouton_beton = pygame.image.load(raccourci+"sprite\\bouton_beton.png").convert()
bouton_bloc_dirigeable = pygame.image.load(raccourci+"sprite\\bouton_bloc_dirigeable.png").convert()
bouton_bois = pygame.image.load(raccourci+"sprite\\bouton_bois.png").convert()
bouton_boue = pygame.image.load(raccourci+"sprite\\bouton_boue.png").convert()
bouton_capteur_air = pygame.image.load(raccourci+"sprite\\bouton_capteur_air.png").convert()
bouton_capteur_chaleur = pygame.image.load(raccourci+"sprite\\bouton_capteur_chaleur.png").convert()
bouton_capteur_froid = pygame.image.load(raccourci+"sprite\\bouton_capteur_froid.png").convert()
bouton_capteur_gaz = pygame.image.load(raccourci+"sprite\\bouton_capteur_gaz.png").convert()
bouton_capteur_humain = pygame.image.load(raccourci+"sprite\\bouton_capteur_humain.png").convert()
bouton_capteur_liquide = pygame.image.load(raccourci+"sprite\\bouton_capteur_liquide.png").convert()
bouton_eau = pygame.image.load(raccourci+"sprite\\bouton_eau.png").convert()
bouton_electricite = pygame.image.load(raccourci+"sprite\\bouton_electricite.png").convert()
bouton_feu = pygame.image.load(raccourci+"sprite\\bouton_feu.png").convert()
bouton_gaz = pygame.image.load(raccourci+"sprite\\bouton_gaz.png").convert()
bouton_glace = pygame.image.load(raccourci+"sprite\\bouton_glace.png").convert()
bouton_graine = pygame.image.load(raccourci+"sprite\\bouton_graine.png").convert()
bouton_humain = pygame.image.load(raccourci+"sprite\\bouton_humain.png").convert()
bouton_lampe = pygame.image.load(raccourci+"sprite\\bouton_lampe.png").convert()
bouton_laser = pygame.image.load(raccourci+"sprite\\bouton_laser.png").convert()
bouton_lave = pygame.image.load(raccourci+"sprite\\bouton_lave.png").convert()
bouton_metal = pygame.image.load(raccourci+"sprite\\bouton_metal.png").convert()
bouton_multi = pygame.image.load(raccourci+"sprite\\bouton_multi.png").convert()
bouton_perso = pygame.image.load(raccourci+"sprite\\bouton_perso.png").convert()
bouton_petrole = pygame.image.load(raccourci+"sprite\\bouton_petrole.png").convert()
bouton_pierre = pygame.image.load(raccourci+"sprite\\bouton_pierre.png").convert()
bouton_pierre_electricite = pygame.image.load(raccourci+"sprite\\bouton_pierre_electricite.png").convert()
bouton_pierre_explosion = pygame.image.load(raccourci+"sprite\\bouton_pierre_explosion.png").convert()
bouton_pierre_feu = pygame.image.load(raccourci+"sprite\\bouton_pierre_feu.png").convert()
bouton_pierre_glace = pygame.image.load(raccourci+"sprite\\bouton_pierre_glace.png").convert()
bouton_pile = pygame.image.load(raccourci+"sprite\\bouton_pile.png").convert()
bouton_poison = pygame.image.load(raccourci+"sprite\\bouton_poison.png").convert()
bouton_pont = pygame.image.load(raccourci+"sprite\\bouton_pont.png").convert()
bouton_porte = pygame.image.load(raccourci+"sprite\\bouton_porte.png").convert()
bouton_radiateur = pygame.image.load(raccourci+"sprite\\bouton_radiateur.png").convert()
bouton_refrigirateur = pygame.image.load(raccourci+"sprite\\bouton_refrigirateur.png").convert()
bouton_sable = pygame.image.load(raccourci+"sprite\\bouton_sable.png").convert()
bouton_terre = pygame.image.load(raccourci+"sprite\\bouton_terre.png").convert()
bouton_tnt = pygame.image.load(raccourci+"sprite\\bouton_tnt.png").convert()
bouton_vapeur = pygame.image.load(raccourci+"sprite\\bouton_vapeur.png").convert()
bouton_verre = pygame.image.load(raccourci+"sprite\\bouton_verre.png").convert()
bouton_vide = pygame.image.load(raccourci+"sprite\\bouton_vide.png").convert()

grille = []
for i in range (6000) :
    grille += ["rien"]
temperature = []
for i in range (6000) :
    temperature += [0]

ecran = 0
outil = 1
pause = 0
appuie = 0
element = "beton"
son = 1
m = 1
couleurs_hum = [(0,0,0),(239,228,176),(255,127,39),(0,85,85),(237,28,36),(0,0,128),(255,201,14),(255,127,39),(139,0,21),(142,88,60)]

alphabet_qwerty = "1234567890qwertyuiopasdfghjkl;zxcvbnm "
alphabet_azerty = "1234567890azertyuiopqsdfghjklmwxcvbn, "

affichage()

pygame.key.set_repeat(50,50)

b = 1
while b == 1 :
    if son == 1 and pygame.mixer.music.get_busy() == False :
        if ecran == 0 :
            pygame.mixer.music.load(raccourci+"sons\\AnDgele.mp3")
        elif ecran == 1 or ecran == 2 or ecran == 3 or ecran == 4 or ecran == 5 :
            if m == 1 :
                pygame.mixer.music.load(raccourci+"sons\\Hyrale.mp3")
                m = 2
            else :
                pygame.mixer.music.load(raccourci+"sons\\Minecraft_OST.mp3")
                m = 1
        pygame.mixer.music.play()

    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()

        elif event.type == MOUSEMOTION :
            if appuie == 1 :
                if outil == 1 and not element == "electricite" and not element == "porte" :
                    grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = element
                elif outil == 1 and element == "electricite" and grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] == "metal" :
                    grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = "electricitem0"
                elif outil == 1 and element == "porte" :
                    ajout_porte = [event.pos[0]//10,(event.pos[1]-50)//10,1,1]
                    if not ajout_porte[1] > 0 :
                        if ajout_porte[0] < 99 :
                            ajout_porte[2] = 2
                        elif ajout_porte[1] < 59 :
                            ajout_porte[2] = 3
                        elif ajout_porte[0] > 0 :
                            ajout_porte[2] = 4
                    ecran = 5
                elif outil == 2 :
                    grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = "rien"

        elif event.type == MOUSEBUTTONUP :
            appuie = 0

        elif event.type == MOUSEBUTTONDOWN :
            if ecran == 0 :
                if event.pos[0] > 371 and event.pos[0] < 626 and event.pos[1] > 509 and event.pos[1] < 575 :
                    ecran = 1
                    pygame.mixer.music.stop()
            elif ecran == 1 :
                if event.pos[0] > 5 and event.pos[0] < 45 and event.pos[1] > 5 and event.pos[1] < 45 :
                    outil = 1
                elif event.pos[0] > 55 and event.pos[0] < 95 and event.pos[1] > 5 and event.pos[1] < 45 :
                    outil = 2
                elif event.pos[0] > 105 and event.pos[0] < 150 and event.pos[1] > 5 and event.pos[1] < 45 :
                    grille = []
                    for i in range (6000) :
                        grille += ["rien"]
                    pause = 0
                    outil = 1
                elif event.pos[0] > 160 and event.pos[0] < 205 and event.pos[1] > 5 and event.pos[1] < 45 :
                    ecran = 3
                    nom = ""
                elif event.pos[0] > 210 and event.pos[0] < 255 and event.pos[1] > 5 and event.pos[1] < 45 :
                    ecran = 4
                    nom = ""
                elif event.pos[0] > 265 and event.pos[0] < 310 and event.pos[1] > 5 and event.pos[1] < 45 :
                    if son == 1 :
                        son = 0
                        pygame.mixer.music.stop()
                    else :
                        son = 1
                elif event.pos[0] > 480 and event.pos[0] < 520 and event.pos[1] > 5 and event.pos[1] < 45 :
                    if pause == 0 :
                        pause = 1
                    else :
                        pause = 0
                elif event.pos[0] > 955 and event.pos[0] < 995 and event.pos[1] > 5 and event.pos[1] < 45 :
                    ecran = 2
                elif event.pos[1] > 50 :
                    if outil == 1 and not element == "electricite" and not element == "porte" :
                        grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = element
                    elif outil == 1 and element == "electricite" and grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] == "metal" :
                        grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = "electricitem0"
                    elif outil == 1 and element == "porte" :
                        ajout_porte = [event.pos[0]//10,(event.pos[1]-50)//10,1,1]
                        if not ajout_porte[1] > 0 :
                            if ajout_porte[0] < 99 :
                                ajout_porte[2] = 2
                            elif ajout_porte[1] < 59 :
                                ajout_porte[2] = 3
                            elif ajout_porte[0] > 0 :
                                ajout_porte[2] = 4
                        ecran = 5
                    elif outil == 2 :
                        grille[event.pos[0]//10+100*((event.pos[1]-50)//10)] = "rien"
                    appuie = 1

            elif ecran == 2 :
                if event.pos[0] > 5 and event.pos[0] < 45 and event.pos[1] > 5 and event.pos[1] < 45 :
                    ecran = 1
                elif event.pos[0] > 7 and event.pos[0] < 47 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "beton"
                elif event.pos[0] > 52 and event.pos[0] < 92 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "bdirigeable"
                elif event.pos[0] > 97 and event.pos[0] < 137 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "bois"
                elif event.pos[0] > 142 and event.pos[0] < 182 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "boue"
                elif event.pos[0] > 187 and event.pos[0] < 227 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "cair0"
                elif event.pos[0] > 232 and event.pos[0] < 272 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "cchaleur0"
                elif event.pos[0] > 277 and event.pos[0] < 317 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "cfroid0"
                elif event.pos[0] > 322 and event.pos[0] < 362 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "cgaz0"
                elif event.pos[0] > 367 and event.pos[0] < 407 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "chum0"
                elif event.pos[0] > 412 and event.pos[0] < 452 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "cliquide0"
                elif event.pos[0] > 457 and event.pos[0] < 497 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "eau"
                elif event.pos[0] > 502 and event.pos[0] < 542 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "electricite"
                elif event.pos[0] > 547 and event.pos[0] < 587 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "feu2"
                elif event.pos[0] > 592 and event.pos[0] < 632 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "gaz"
                elif event.pos[0] > 637 and event.pos[0] < 677 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "glace"
                elif event.pos[0] > 682 and event.pos[0] < 722 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "graine"
                elif event.pos[0] > 727 and event.pos[0] < 767 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "hum"
                elif event.pos[0] > 772 and event.pos[0] < 812 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "lampef0"
                elif event.pos[0] > 817 and event.pos[0] < 857 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "laser"
                elif event.pos[0] > 862 and event.pos[0] < 902 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "lave"
                elif event.pos[0] > 907 and event.pos[0] < 947 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "metal"
                elif event.pos[0] > 952 and event.pos[0] < 992 and event.pos[1] > 55 and event.pos[1] < 95 :
                    element = "multi"
                elif event.pos[0] > 7 and event.pos[0] < 47 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "perso"
                elif event.pos[0] > 52 and event.pos[0] < 92 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "petrolee"
                elif event.pos[0] > 97 and event.pos[0] < 137 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pierre"
                elif event.pos[0] > 142 and event.pos[0] < 182 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pelectricite01"
                elif event.pos[0] > 187 and event.pos[0] < 227 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pexplosion01"
                elif event.pos[0] > 232 and event.pos[0] < 272 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pfeu01"
                elif event.pos[0] > 277 and event.pos[0] < 317 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pglace01"
                elif event.pos[0] > 322 and event.pos[0] < 362 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pile3"
                elif event.pos[0] > 367 and event.pos[0] < 407 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "poison"
                elif event.pos[0] > 412 and event.pos[0] < 452 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "pont"
                elif event.pos[0] > 457 and event.pos[0] < 497 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "porte"
                elif event.pos[0] > 502 and event.pos[0] < 542 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "radiateurf0"
                elif event.pos[0] > 547 and event.pos[0] < 587 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "refrigirateurf0"
                elif event.pos[0] > 592 and event.pos[0] < 632 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "sable"
                elif event.pos[0] > 637 and event.pos[0] < 677 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "terre"
                elif event.pos[0] > 682 and event.pos[0] < 722 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "tnt"
                elif event.pos[0] > 727 and event.pos[0] < 767 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "vapeur"
                elif event.pos[0] > 772 and event.pos[0] < 812 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "verre"
                elif event.pos[0] > 817 and event.pos[0] < 857 and event.pos[1] > 100 and event.pos[1] < 145 :
                    element = "vide"

            elif ecran == 3 or ecran == 4 :
                if event.pos[0] < 390 or event.pos[0] > 610 or event.pos[1] < 280 or event.pos[1] > 345 :
                    ecran = 1

        elif event.type == KEYDOWN :
            if ecran == 1 :
                if event.key == K_UP :
                    for i in range (len(grille)) :
                        if i > 99 and grille[i] == "bdirigeable" and (grille[i-100] == "rien" or grille[i-100][0:3] == "feu" or len(grille[i-100]) == 6 and grille[i-100][0:5] == "laser") :
                            grille[i-100] = grille[i]
                            grille[i] = "rien"
                        elif i > 99 and grille[i] == "bdirigeable" and (grille[i-100] == "eau" or grille[i-100] == "eau_toxique" or grille[i-100] == "lave" or grille[i-100] == "petrolee" or grille[i-100] == "petrolea" or grille[i-100] == "poison" or grille[i-100] == "vapeur" or grille[i-100] == "gaz") :
                            grille[i],grille[i-100] = grille[i-100],grille[i]
                        elif len(grille[i]) == 7 and grille[i][0:5] == "perso" :
                            if grille[i][6] == "0" and (i < 5900 and not grille[i+100] == "rien" and not grille[i+100][0:3] == "feu" and not (len(grille[i+100]) == 6 and grille[i+100][0:5] == "laser") and not (grille[i][5] == "1" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu" or len(grille[i+100]) == 6 and grille[i+100][0:5] == "laser")) or i > 5899) :
                                grille[i] = grille[i][0:6]+"6"
                elif event.key == K_DOWN :
                    for i in range (len(grille)-1,-1,-1) :
                        if i < 5900 and grille[i] == "bdirigeable" and (grille[i+100] == "rien" or grille[i+100][0:3] == "feu" or len(grille[i+100]) == 6 and grille[i+100][0:5] == "laser") :
                            grille[i+100] = grille[i]
                            grille[i] = "rien"
                        elif i < 5900 and grille[i] == "bdirigeable" and (grille[i+100] == "eau" or grille[i+100] == "eau_toxique" or grille[i+100] == "lave" or grille[i+100] == "petrolee" or grille[i+100] == "petrolea" or grille[i+100] == "poison" or grille[i+100] == "vapeur" or grille[i+100] == "gaz") :
                            grille[i],grille[i+100] = grille[i+100],grille[i]
                elif event.key == K_LEFT :
                    for i in range (len(grille)) :
                        if i-(i//100)*100 > 0 and grille[i] == "bdirigeable" and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu" or len(grille[i-1]) == 6 and grille[i-1][0:5] == "laser") :
                            grille[i-1] = grille[i]
                            grille[i] = "rien"
                        elif i-(i//100)*100 > 0 and grille[i] == "bdirigeable" and (grille[i-1] == "eau" or grille[i-1] == "eau_toxique" or grille[i-1] == "lave" or grille[i-1] == "petrolee" or grille[i-1] == "petrolea" or grille[i-1] == "poison" or grille[i-1] == "vapeur" or grille[i-1] == "gaz") :
                            grille[i],grille[i-1] = grille[i-1],grille[i]
                        elif len(grille[i]) == 7 and grille[i][0:5] == "perso" :
                            if grille[i][5] == "1" :
                                if i-(i//100)*100 > 0 and (grille[i-1] == "rien" or grille[i-1][0:3] == "feu" or len(grille[i-1]) == 6 and grille[i-1][0:5] == "laser") and (grille[i-101] == "rien" or grille[i-101][0:3] == "feu" or len(grille[i-101]) == 6 and grille[i-101][0:5] == "laser") and (grille[i-201] == "rien" or grille[i-201][0:3] == "feu" or len(grille[i-201]) == 6 and grille[i-201][0:5] == "laser") and (grille[i-301] == "rien" or grille[i-301][0:3] == "feu" or len(grille[i-301]) == 6 and grille[i-301][0:5] == "laser") and (grille[i-401] == "rien" or grille[i-401][0:3] == "feu" or len(grille[i-401]) == 6 and grille[i-401][0:5] == "laser") and (grille[i-501] == "rien" or grille[i-501][0:3] == "feu" or len(grille[i-501]) == 6 and grille[i-501][0:5] == "laser") :
                                    grille[i] += "0"
                                    for j in range (6) :
                                        grille[(i-1)-j*100] = grille[i-j*100]
                                        grille[i-j*100] = grille[(i+1)-j*100]
                                        grille[(i+1)-j*100] = "rien"
                                elif i-(i//100)*100 > 0 and (grille[i-1] == "eau" or grille[i-1] == "eau_toxique" or grille[i-1] == "lave" or grille[i-1] == "petrolee" or grille[i-1] == "petrolea" or grille[i-1] == "poison" or grille[i-1] == "vapeur" or grille[i-1] == "gaz" or grille[i-1] == "rien" or grille[i-1][0:3] == "feu") and (grille[i-101] == "eau" or grille[i-101] == "eau_toxique" or grille[i-101] == "lave" or grille[i-101] == "petrolee" or grille[i-101] == "petrolea" or grille[i-101] == "poison" or grille[i-101] == "vapeur" or grille[i-101] == "gaz" or grille[i-101] == "rien" or grille[i-101][0:3] == "feu") and (grille[i-201] == "eau" or grille[i-201] == "eau_toxique" or grille[i-201] == "lave" or grille[i-201] == "petrolee" or grille[i-201] == "petrolea" or grille[i-201] == "poison" or grille[i-201] == "vapeur" or grille[i-201] == "gaz" or grille[i-201] == "rien" or grille[i-201][0:3] == "feu") and (grille[i-301] == "eau" or grille[i-301] == "eau_toxique" or grille[i-301] == "lave" or grille[i-301] == "petrolee" or grille[i-301] == "petrolea" or grille[i-301] == "poison" or grille[i-301] == "vapeur" or grille[i-301] == "gaz" or grille[i-301] == "rien" or grille[i-301][0:3] == "feu") and (grille[i-401] == "eau" or grille[i-401] == "eau_toxique" or grille[i-401] == "lave" or grille[i-401] == "petrolee" or grille[i-401] == "petrolea" or grille[i-401] == "poison" or grille[i-401] == "vapeur" or grille[i-401] == "gaz" or grille[i-401] == "rien" or grille[i-401][0:3] == "feu") and (grille[i-501] == "eau" or grille[i-501] == "eau_toxique" or grille[i-501] == "lave" or grille[i-501] == "petrolee" or grille[i-501] == "petrolea" or grille[i-501] == "poison" or grille[i-501] == "vapeur" or grille[i-501] == "gaz" or grille[i-501] == "rien" or grille[i-501][0:3] == "feu") :
                                    grille[i] += "0"
                                    for j in range (6) :
                                        grille[(i-1)-j*100],grille[i-j*100] = grille[i-j*100],grille[(i-1)-j*100]
                                        grille[i-j*100],grille[(i+1)-j*100] = grille[(i+1)-j*100],grille[i-j*100]
                                elif i-(i//100)*100 > 0 and i > 99 and (grille[i-600] == "rien" or grille[i-600][0:3] == "feu" or len(grille[i-600]) == 6 and grille[i-600][0:5] == "laser") and (grille[i-101] == "rien" or grille[i-101][0:3] == "feu" or len(grille[i-101]) == 6 and grille[i-101][0:5] == "laser") and (grille[i-201] == "rien" or grille[i-201][0:3] == "feu" or len(grille[i-201]) == 6 and grille[i-201][0:5] == "laser") and (grille[i-301] == "rien" or grille[i-301][0:3] == "feu" or len(grille[i-301]) == 6 and grille[i-301][0:5] == "laser") and (grille[i-401] == "rien" or grille[i-401][0:3] == "feu" or len(grille[i-401]) == 6 and grille[i-401][0:5] == "laser") and (grille[i-501] == "rien" or grille[i-501][0:3] == "feu" or len(grille[i-501]) == 6 and grille[i-501][0:5] == "laser") and (grille[i-601] == "rien" or grille[i-601][0:3] == "feu" or len(grille[i-601]) == 6 and grille[i-601][0:5] == "laser") :
                                    grille[i] += "0"
                                    for j in range (5,-1,-1) :
                                        grille[(i-1)-(j+1)*100] = grille[i-j*100]
                                        grille[i-(j+1)*100] = grille[(i+1)-j*100]
                                        grille[i-j*100] = "rien"
                                        grille[(i+1)-j*100] = "rien"
                                elif i-(i//100)*100 > 0 and i > 99 and (grille[i-600] == "eau" or grille[i-600] == "eau_toxique" or grille[i-600] == "lave" or grille[i-600] == "petrolee" or grille[i-600] == "petrolea" or grille[i-600] == "poison" or grille[i-600] == "vapeur" or grille[i-600] == "gaz" or grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i-101] == "eau" or grille[i-101] == "eau_toxique" or grille[i-101] == "lave" or grille[i-101] == "petrolee" or grille[i-101] == "petrolea" or grille[i-101] == "poison" or grille[i-101] == "vapeur" or grille[i-101] == "gaz" or grille[i-101] == "rien" or grille[i-101][0:3] == "feu") and (grille[i-201] == "eau" or grille[i-201] == "eau_toxique" or grille[i-201] == "lave" or grille[i-201] == "petrolee" or grille[i-201] == "petrolea" or grille[i-201] == "poison" or grille[i-201] == "vapeur" or grille[i-201] == "gaz" or grille[i-201] == "rien" or grille[i-201][0:3] == "feu") and (grille[i-301] == "eau" or grille[i-301] == "eau_toxique" or grille[i-301] == "lave" or grille[i-301] == "petrolee" or grille[i-301] == "petrolea" or grille[i-301] == "poison" or grille[i-301] == "vapeur" or grille[i-301] == "gaz" or grille[i-301] == "rien" or grille[i-301][0:3] == "feu") and (grille[i-401] == "eau" or grille[i-401] == "eau_toxique" or grille[i-401] == "lave" or grille[i-401] == "petrolee" or grille[i-401] == "petrolea" or grille[i-401] == "poison" or grille[i-401] == "vapeur" or grille[i-401] == "gaz" or grille[i-401] == "rien" or grille[i-401][0:3] == "feu") and (grille[i-501] == "eau" or grille[i-501] == "eau_toxique" or grille[i-501] == "lave" or grille[i-501] == "petrolee" or grille[i-501] == "petrolea" or grille[i-501] == "poison" or grille[i-501] == "vapeur" or grille[i-501] == "gaz" or grille[i-501] == "rien" or grille[i-501][0:3] == "feu") and (grille[i-601] == "eau" or grille[i-601] == "eau_toxique" or grille[i-601] == "lave" or grille[i-601] == "petrolee" or grille[i-601] == "petrolea" or grille[i-601] == "poison" or grille[i-601] == "vapeur" or grille[i-601] == "gaz" or grille[i-601] == "rien" or grille[i-601][0:3] == "feu") :
                                    grille[i] += "0"
                                    for j in range (5,-1,-1) :
                                        grille[(i-1)-(j+1)*100],grille[i-j*100] = grille[i-j*100],grille[(i-1)-(j+1)*100]
                                        grille[i-(j+1)*100],grille[(i+1)-j*100] = grille[(i+1)-j*100],grille[i-(j+1)*100]
                            else :
                                grille[i] = "perso1"+grille[i][6]+"0"
                                for j in range (6) :
                                    grille[i-j*100],grille[(i-1)-j*100] = grille[(i-1)-j*100],grille[i-j*100]
                    for i in range (len(grille)) :
                        if len(grille[i]) == 8 and grille[i][0:5] == "perso" :
                            grille[i] = grille[i][0:7]

                elif event.key == K_RIGHT :
                    for i in range (len(grille)-1,-1,-1) :
                        if i-(i//100)*100 < 99 and grille[i] == "bdirigeable" and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu" or len(grille[i+1]) == 6 and grille[i+1][0:5] == "laser") :
                            grille[i+1] = grille[i]
                            grille[i] = "rien"
                        elif i-(i//100)*100 < 99 and grille[i] == "bdirigeable" and (grille[i+1] == "eau" or grille[i+1] == "eau_toxique" or grille[i+1] == "lave" or grille[i+1] == "petrolee" or grille[i+1] == "petrolea" or grille[i+1] == "poison" or grille[i+1] == "vapeur" or grille[i+1] == "gaz") :
                            grille[i],grille[i+1] = grille[i+1],grille[i]
                        elif len(grille[i]) == 7 and grille[i][0:5] == "perso" :
                            if grille[i][5] == "2" :
                                if i-(i//100)*100 < 99 and (grille[i+1] == "rien" or grille[i+1][0:3] == "feu" or len(grille[i+1]) == 6 and grille[i+1][0:5] == "laser") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu" or len(grille[i-99]) == 6 and grille[i-99][0:5] == "laser") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu" or len(grille[i-199]) == 6 and grille[i-199][0:5] == "laser") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu" or len(grille[i-299]) == 6 and grille[i-299][0:5] == "laser") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu" or len(grille[i-399]) == 6 and grille[i-399][0:5] == "laser") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu" or len(grille[i-499]) == 6 and grille[i-499][0:5] == "laser") :
                                    grille[i] += "0"
                                    for j in range (6) :
                                        grille[(i+1)-j*100] = grille[i-j*100]
                                        grille[i-j*100] = grille[(i-1)-j*100]
                                        grille[(i-1)-j*100] = "rien"
                                elif i-(i//100)*100 < 99 and (grille[i+1] == "eau" or grille[i+1] == "eau_toxique" or grille[i+1] == "lave" or grille[i+1] == "petrolee" or grille[i+1] == "petrolea" or grille[i+1] == "poison" or grille[i+1] == "vapeur" or grille[i+1] == "gaz" or grille[i+1] == "rien" or grille[i+1][0:3] == "feu") and (grille[i-99] == "eau" or grille[i-99] == "eau_toxique" or grille[i-99] == "lave" or grille[i-99] == "petrolee" or grille[i-99] == "petrolea" or grille[i-99] == "poison" or grille[i-99] == "vapeur" or grille[i-99] == "gaz" or grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i-199] == "eau" or grille[i-199] == "eau_toxique" or grille[i-199] == "lave" or grille[i-199] == "petrolee" or grille[i-199] == "petrolea" or grille[i-199] == "poison" or grille[i-199] == "vapeur" or grille[i-199] == "gaz" or grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-299] == "eau" or grille[i-299] == "eau_toxique" or grille[i-299] == "lave" or grille[i-299] == "petrolee" or grille[i-299] == "petrolea" or grille[i-299] == "poison" or grille[i-299] == "vapeur" or grille[i-299] == "gaz" or grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-399] == "eau" or grille[i-399] == "eau_toxique" or grille[i-399] == "lave" or grille[i-399] == "petrolee" or grille[i-399] == "petrolea" or grille[i-399] == "poison" or grille[i-399] == "vapeur" or grille[i-399] == "gaz" or grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-499] == "eau" or grille[i-499] == "eau_toxique" or grille[i-499] == "lave" or grille[i-499] == "petrolee" or grille[i-499] == "petrolea" or grille[i-499] == "poison" or grille[i-499] == "vapeur" or grille[i-499] == "gaz" or grille[i-499] == "rien" or grille[i-499][0:3] == "feu") :
                                    grille[i] += "0"
                                    for j in range (6) :
                                        grille[(i+1)-j*100],grille[i-j*100] = grille[i-j*100],grille[(i+1)-j*100]
                                        grille[i-j*100],grille[(i-1)-j*100] = grille[(i-1)-j*100],grille[i-j*100]
                                elif i-(i//100)*100 < 99 and i > 99 and (grille[i-600] == "rien" or grille[i-600][0:3] == "feu" or len(grille[i-600]) == 6 and grille[i-600][0:5] == "laser") and (grille[i-99] == "rien" or grille[i-99][0:3] == "feu" or len(grille[i-99]) == 6 and grille[i-99][0:5] == "laser") and (grille[i-199] == "rien" or grille[i-199][0:3] == "feu" or len(grille[i-199]) == 6 and grille[i-199][0:5] == "laser") and (grille[i-299] == "rien" or grille[i-299][0:3] == "feu" or len(grille[i-299]) == 6 and grille[i-299][0:5] == "laser") and (grille[i-399] == "rien" or grille[i-399][0:3] == "feu" or len(grille[i-399]) == 6 and grille[i-399][0:5] == "laser") and (grille[i-499] == "rien" or grille[i-499][0:3] == "feu" or len(grille[i-499]) == 6 and grille[i-499][0:5] == "laser") and (grille[i-599] == "rien" or grille[i-599][0:3] == "feu" or len(grille[i-599]) == 6 and grille[i-599][0:5] == "laser") :
                                    grille[i] += "0"
                                    for j in range (5,-1,-1) :
                                        grille[(i+1)-(j+1)*100] = grille[i-j*100]
                                        grille[i-(j+1)*100] = grille[(i-1)-j*100]
                                        grille[i-j*100] = "rien"
                                        grille[(i-1)-j*100] = "rien"
                                elif i-(i//100)*100 < 99 and i > 99 and (grille[i-600] == "eau" or grille[i-600] == "eau_toxique" or grille[i-600] == "lave" or grille[i-600] == "petrolee" or grille[i-600] == "petrolea" or grille[i-600] == "poison" or grille[i-600] == "vapeur" or grille[i-600] == "gaz" or grille[i-600] == "rien" or grille[i-600][0:3] == "feu") and (grille[i-99] == "eau" or grille[i-99] == "eau_toxique" or grille[i-99] == "lave" or grille[i-99] == "petrolee" or grille[i-99] == "petrolea" or grille[i-99] == "poison" or grille[i-99] == "vapeur" or grille[i-99] == "gaz" or grille[i-99] == "rien" or grille[i-99][0:3] == "feu") and (grille[i-199] == "eau" or grille[i-199] == "eau_toxique" or grille[i-199] == "lave" or grille[i-199] == "petrolee" or grille[i-199] == "petrolea" or grille[i-199] == "poison" or grille[i-199] == "vapeur" or grille[i-199] == "gaz" or grille[i-199] == "rien" or grille[i-199][0:3] == "feu") and (grille[i-299] == "eau" or grille[i-299] == "eau_toxique" or grille[i-299] == "lave" or grille[i-299] == "petrolee" or grille[i-299] == "petrolea" or grille[i-299] == "poison" or grille[i-299] == "vapeur" or grille[i-299] == "gaz" or grille[i-299] == "rien" or grille[i-299][0:3] == "feu") and (grille[i-399] == "eau" or grille[i-399] == "eau_toxique" or grille[i-399] == "lave" or grille[i-399] == "petrolee" or grille[i-399] == "petrolea" or grille[i-399] == "poison" or grille[i-399] == "vapeur" or grille[i-399] == "gaz" or grille[i-399] == "rien" or grille[i-399][0:3] == "feu") and (grille[i-499] == "eau" or grille[i-499] == "eau_toxique" or grille[i-499] == "lave" or grille[i-499] == "petrolee" or grille[i-499] == "petrolea" or grille[i-499] == "poison" or grille[i-499] == "vapeur" or grille[i-499] == "gaz" or grille[i-499] == "rien" or grille[i-499][0:3] == "feu") and (grille[i-599] == "eau" or grille[i-599] == "eau_toxique" or grille[i-599] == "lave" or grille[i-599] == "petrolee" or grille[i-599] == "petrolea" or grille[i-599] == "poison" or grille[i-599] == "vapeur" or grille[i-599] == "gaz" or grille[i-599] == "rien" or grille[i-599][0:3] == "feu") :
                                    grille[i] += "0"
                                    for j in range (5,-1,-1) :
                                        grille[(i+1)-(j+1)*100],grille[i-j*100] = grille[i-j*100],grille[(i+1)-(j+1)*100]
                                        grille[i-(j+1)*100],grille[(i-1)-j*100] = grille[(i-1)-j*100],grille[i-(j+1)*100]
                            else :
                                grille[i] = "perso2"+grille[i][6]+"0"
                                for j in range (6) :
                                    grille[i-j*100],grille[(i+1)-j*100] = grille[(i+1)-j*100],grille[i-j*100]
                    for i in range (len(grille)) :
                        if len(grille[i]) == 8 and grille[i][0:5] == "perso" :
                            grille[i] = grille[i][0:7]
            elif ecran == 3 or ecran == 4 :
                if event.key == K_BACKSPACE and len(nom) > 0 :
                    nom = nom[0:len(nom)-1]
                elif event.key == K_RETURN and len(nom) > 0 :
                    sauvegarde()
                else :
                    i = 0
                    non = 0
                    while i < len(alphabet_qwerty) and non == 0 :
                        if alphabet_qwerty[i] == chr(event.key) :
                            non = 1
                        i += 1
                    if non == 1 and not alphabet_azerty[i-1] == "," and len(nom) < 17 :
                        nom += alphabet_azerty[i-1]
            elif ecran == 5 :
                if event.key == K_UP and ajout_porte[1] > 0 :
                    if not ajout_porte[2] == 1 :
                        ajout_porte[2],ajout_porte[3] = 1,1
                    elif ajout_porte[1]-ajout_porte[3] > 0 :
                        ajout_porte[3] += 1
                elif event.key == K_RIGHT and ajout_porte[0] < 99 :
                    if not ajout_porte[2] == 2 :
                        ajout_porte[2],ajout_porte[3] = 2,1
                    elif ajout_porte[0]+ajout_porte[3] < 99 :
                        ajout_porte[3] += 1
                elif event.key == K_DOWN and ajout_porte[1] < 59 :
                    if not ajout_porte[2] == 3 :
                        ajout_porte[2],ajout_porte[3] = 3,1
                    elif ajout_porte[1]+ajout_porte[3] < 59 :
                        ajout_porte[3] += 1
                elif event.key == K_LEFT and ajout_porte[0] > 0 :
                    if not ajout_porte[2] == 4 :
                        ajout_porte[2],ajout_porte[3] = 4,1
                    elif ajout_porte[0]-ajout_porte[3] > 0 :
                        ajout_porte[3] += 1
                elif event.key == K_RETURN :
                    grille[ajout_porte[0]+100*ajout_porte[1]] = "porte0"+str(ajout_porte[2])+str(ajout_porte[3])
                    if ajout_porte[2] == 1 :
                        for i in range (1,ajout_porte[3]+1) :
                            grille[ajout_porte[0]+100*(ajout_porte[1]-i)] = "porte"
                    elif ajout_porte[2] == 2 :
                        for i in range (1,ajout_porte[3]+1) :
                            grille[ajout_porte[0]+i+100*ajout_porte[1]] = "porte"
                    elif ajout_porte[2] == 3 :
                        for i in range (1,ajout_porte[3]+1) :
                            grille[ajout_porte[0]+100*(ajout_porte[1]+i)] = "porte"
                    elif ajout_porte[2] == 4 :
                        for i in range (1,ajout_porte[3]+1) :
                            grille[ajout_porte[0]-i+100*ajout_porte[1]] = "porte"
                    ecran = 1
                elif event.key == K_ESCAPE :
                    ecran = 1

    affichage()

    if ecran == 1 and pause == 0 :
        mouv_blocs()