#sumar listas
def lista(lista1, lista2):
    if isinstance((lista1, list) and isinstance(lista2, list)and len (lista1) == len(lista2)):
        return lista_aux(lista1, lista2)
    else:
        return "Error: el valor ingresado no es una lista"
def lista_aux(lista,lista2):
    if lista1  == [] and lista2 == []:
        return []
    else:
        return [lista1[0] + lista2[0]] + lista_aux[lista1[1:], lista2[1:]])
