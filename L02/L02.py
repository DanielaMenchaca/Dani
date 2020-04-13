# -*- coding: utf-8 -*-
"""L02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fh0-3KDSs2-LqUK0EDVt6Ypwxa6orE2j
"""

def sup_de_nivel(mapa,celda,recorrido):
    recorrido.append(celda)
    nij = mapa[celda[0]][celda[1]]
    
    if celda[0]-1 >= 0:
        if celda[1]-1 >= 0:
            if mapa[celda[0]-1][celda[1]-1] == nij and (celda[0]-1,celda[1]-1) not in recorrido:
                sup_de_nivel(mapa,(celda[0]-1,celda[1]-1),recorrido)
        if mapa[celda[0]-1][celda[1]] == nij and (celda[0]-1,celda[1]) not in recorrido:
            sup_de_nivel(mapa,(celda[0]-1,celda[1]),recorrido)
        if celda[1]+1 < len(mapa[0]):
            if mapa[celda[0]-1][celda[1]+1] == nij and (celda[0]-1,celda[1]+1) not in recorrido:
                sup_de_nivel(mapa,(celda[0]-1,celda[1]+1),recorrido)
                
    if celda[0]+1 < len(mapa):
        if celda[1]-1 >= 0:
            if mapa[celda[0]+1][celda[1]-1] == nij and (celda[0]+1,celda[1]-1) not in recorrido:
                sup_de_nivel(mapa,(celda[0]+1,celda[1]-1),recorrido)
        if mapa[celda[0]+1][celda[1]] == nij and (celda[0]+1,celda[1]) not in recorrido:
            sup_de_nivel(mapa,(celda[0]+1,celda[1]),recorrido)
        if celda[1]+1 < len(mapa[0]):
            if mapa[celda[0]+1][celda[1]+1] == nij and (celda[0]+1,celda[1]+1) not in recorrido:
                sup_de_nivel(mapa,(celda[0]+1,celda[1]+1),recorrido)
                
    if celda[1]+1 < len(mapa[0]):
        if mapa[celda[0]][celda[1]+1] == nij and (celda[0],celda[1]+1) not in recorrido:
                sup_de_nivel(mapa,(celda[0],celda[1]+1),recorrido)
    
    if celda[1]-1 >= 0:
        if mapa[celda[0]][celda[1]-1] == nij and (celda[0],celda[1]-1) not in recorrido:
                sup_de_nivel(mapa,(celda[0],celda[1]-1),recorrido)

def superficie_de_nivel(mapa,celda):
    recorrido = []
    sup_de_nivel(mapa,celda,recorrido)
    recorrido.sort()
    return (recorrido)

def son_anagramas(string1, string2):
    diccionario = dict()
    dicc = dict()
    if len(string1) != len(string2):
        return (False)
    else:
        for i in string1:
            if i not in diccionario:
                diccionario[i] = 0
            else:
                diccionario[i] += 1
        for i in string2:
            if i not in dicc:
                dicc[i] = 0
            else:
                dicc[i] += 1
        if diccionario.items() == dicc.items():
            return (True)
        else:
            return (False)

def nuevo_muro(muro):
    desde = 0
    hasta= 0
    desde_ = 0
    subiendo = True
    for i in range(len(muro)-1):      
        if subiendo:
            if muro[i]>muro[i+1]:
                subiendo = False
            if muro[i]==muro[i+1]:
                if hasta-desde < i - desde_:
                    desde=desde_
                    hasta=i
                desde_= i+1
        else:
            if muro[i] <= muro[i+1]:
                subiendo=True
                if hasta-desde < i - desde_:
                    desde=desde_
                    hasta=i
                if muro[i]<muro[i+1]:
                    desde_=i
                if muro[i]==muro[i+1]:
                    desde_=i+1
    if hasta-desde < (len(muro)-1) - desde_:
        desde=desde_
        hasta=len(muro)-1
    return (muro[desde:hasta + 1])