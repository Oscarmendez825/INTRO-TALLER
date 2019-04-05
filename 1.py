#Suma valores de las raiz cuadradas de una lista
import math
def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def suma_aux(lista):
    if lista == []:
        return 0
    else: return math.sqrt(lista[0]) + suma_aux(lista[1:])
