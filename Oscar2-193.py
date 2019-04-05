#Detectar si la lista posee un 0
def cero(lista):
    if isinstance(lista, list):
        return cero_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def cero_aux(lista):
    if lista == []:
        return 0
    elif (lista[0] == 0):
        return Tres
    else:
        return False
