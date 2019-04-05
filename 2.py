def sumaBin(lista1, lista2, acarreo):
    if (isinstance(lista1, list) and isinstance (lista2,list) and len(lista1) == len(lista2) and
        isinstance(acarreo, int)):

        return sumaBin_aux (lista1, lista2, acarreo)
    else: return "Error en la validación"
def sumaBin_aux(lista1, lista2, acarreo):
    if lista1 == [] and lista2 == [] and acarreo >= 0:
        return [acarreo]
    elif (lista1[-1] + lista2[-1] + acarreo) ==2
        return (sumaBin_aux (lista1[:-1], lista2[:-1], 1))+[0]
    elif (lista1[-1] + lista2[-1]+ acarreo)==3:
        return (sumaBin_aux (lista1[:-1], lista2[:-1], 1))+[1]
    else: return (sumaBin_aux (lista1[:-1], lista2[:-1], 0)
