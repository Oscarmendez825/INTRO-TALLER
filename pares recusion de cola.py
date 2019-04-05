#hacer una funcion que reciba una lista y obtenga otra lista con los numeros pares. utilice slicing
def pares(lista):
    cond = lambda lista:lista%2==0
    if isinstance (lista, list) and lista != []:
        return pares_aux(lista, [], cond)
    else: return "ERROR"
def pares_aux(lista, resultado, cond):
    if lista==[]:
        return resultado
    elif cond(lista[0]):
        return pares_aux(lista[1:], resultado + [lista[0]] , cond)
    else: return pares_aux(lista[1:], resultado , cond)
