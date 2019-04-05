def recorrer(lista):
    if isinstance(lista,list):
        return recorrer_aux(lista,0,0)
    else: return "error"

def recorrer_aux(lista, resultado, indice):
    if indice == len(lista):
        return resultado
    elif isinstance(lista[indice],list):
        return recorrer_aux(lista[indice],0,0)+recorrer_aux(lista, resultado, indice+1)
    else:return recorrer_aux(lista, resultado + lista[indice], indice+1)
lista = [5,8,19,[6,[7,8],9,10],11,12]
#lista=[5,6,7,8,9,10,11]
print(recorrer(lista))
