import math
def mediageometrica(lista):
    if isinstance(lista, list):
        return media_aux(lista), media_aux2(lista)
    else: return "Con los valores ingresados no se puede realizar una media geométrica"
def media_aux(lista):
    if (lista == []):
        return 1
    if lista[0] > 0:
        return (lista [0] * media_aux(lista[1:]))
def media_aux2(lista):
    if lista == []:
            return 1
    else:
        return (lista[0] * media_aux(lista[1:])) ** (1/len(lista))-1   
