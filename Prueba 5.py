def listabin(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2, list):
        return 0
    else: return"Error"

def listabin_aux(lista1, lista2):
    if(lista1 == []):
        return 0
    else:
        return ([lista1[0] + lista2[0]] + listabin_aux[lista1[1:], lista2[1:]])%2
