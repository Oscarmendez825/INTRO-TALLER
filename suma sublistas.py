def lista(lista):
    if isinstance(lista, list):
        return lista_aux(lista)
    else:return "LO INGRESADO NO ES UNA LISTA"
def lista_aux(lista):
    if lista==[]:
        return 0
    if isinstance(lista[0], list):
        return lista_aux(lista[0]+lista[1:])
        #return lista_aux(lista[0])+lista_aux(lista[1:])
    else: return lista_aux(lista[1:])+lista[0]
