#suma pares
def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def suma_aux(lista):
    if lista == []:
        return 0
    if ((lista[0] % 2) == 0):
        return lista [0] + suma_aux(lista[1:])
    else: return suma_aux(lista[1:])

#suma impares
def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def suma_aux(lista):
    if lista == []:
        return 0
    if ((lista[0] % 2) == 1):
        return lista [0] + suma_aux(lista[1:])
    else: return suma_aux(lista[1:])
