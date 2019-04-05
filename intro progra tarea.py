import math
def mediageometrica(lista):
    if isinstance(lista, list) and (len(lista)>0):
        return media_aux(lista)**(1/len(lista)), media_aux(lista[1:])
    else: return "Con los valores ingresados no se puede realizar una media geométrica"
def media_aux(lista):
    if (lista == []):
        return []
    else:
        return lista [0] * media_aux(lista[1:])*(1/len(lista))+ media_aux(lista[1:])+lista [0] * media_aux(lista[1:])*(1/len(lista))+ media_aux(lista[1:])

