#hacer unafuncion que multiplique el resultado de multiplicaciones previas usando slicing
def multi(lista):
    if isinstance (lista, list) and lista != []:
        return multi_aux(lista, 1)
    else: return "ERROR"
def multi_aux(lista, resultado):
    if lista==[]:
        return resultado
    else: return multi_aux(lista[1:], resultado * lista[0])
