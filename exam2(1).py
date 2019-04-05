def potencia(lista):
    if isinstance (lista, list):
        return potencia_aux(lista, 1)
    else:return "GRAVE ERROR"
def potencia_aux(lista, exp):
    if lista == []:
        return []
    elif lista[0:]==list:
        return lista[0]+lista[1:]
    else:
        return lista[0]**exp, potencia_aux(lista[1:], exp+1)
    
