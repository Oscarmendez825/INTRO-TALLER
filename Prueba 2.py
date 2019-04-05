#Eliminar el valor indicado
def eliminar(lista, num):
    if isinstance(lista, list):
        return eliminar_aux(lista, num)
    else:
        return "Error: el valor ingresado no es una lista"
def eliminar_aux(lista, num):
    if lista == []:
        return []
    elif (lista[0] == num):
        return eliminar_aux(lista[1:], num)
    else:
        return [lista[0]]+ eliminar_aux(lista[1:], num)
