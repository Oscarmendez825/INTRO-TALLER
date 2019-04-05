#sacar el numero menor de una lista
def minimo(lista):
    if isinstance(lista, list):
        return minimo_aux(lista)
    else:
        return "Error: el valor ingresado no es una lista"
def minimo_aux(lista):
    if lista [1:] == []:
        return lista[0]
    elif lista[0] <= lista[1]:
        return minimo_aux([lista[0]] + lista[2:])
    else:
        return minimo_aux(lista[1:])
