#ordenar de mayor a menor(bubble sort)
def cambiar(lista):
    if isinstance(lista, list) and lista != []:
        return cambiar_aux(lista, 0)
    else: return "GRAVE ERROR HERMANO"
    
def cambiar_aux(lista, indice):
    if indice == len(lista)-1:
        return lista
    else: return cambiar_aux(cambiar2_aux(lista,0), indice + 1)
    
def cambiar2_aux(lista, indice):
    if indice == len(lista)-1:
        return lista
    elif lista[indice] > lista[indice+1]:
            aux = lista[indice]
            lista[indice] = lista[indice+1]
            lista[indice+1] = aux
            return cambiar_aux(lista, indice+1)
    else: return cambiar2_aux(lista, indice+1)
