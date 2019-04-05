#Si hay un número negativo en la lista devolverá falso de lo contrario devolverá verdadero
def positivos_negativos(lista):
    if isinstance(lista, list):
        return positivos_negativos_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def positivos_negativos_aux(lista):
    if lista == []:
        return 0
    elif (lista[0] > 0):
        return True
    else:
        return False
#Profe:
def positivos_negativos(lista):
    if isinstance(lista, list): and lista !=
        return positivos_negativos_aux(lista)
    else:
        return "Error: el valor ingresado n es una lista"
def positivos_negativos_aux(lista):
    if lista == []:
        return True
    elif (lista[0] < 0):
        return False
    else:
        return positivos_negativos_aux(lista[1:])
