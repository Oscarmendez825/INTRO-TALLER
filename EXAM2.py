import math
def std (lista, avg):
    if isinstance(lista,list) and isinstance (avg, float):
        return mah.sqrt(std_aux(lista, avg)/(len(lista)-1)
    else: return "ERROR"
def std_aux(lista, avg):
    if lista==[]:
        return 0
    else: return ((lista[0]-avg)**std_aux(lista[1:], avg)
#--------------------------COLA----------------------------#
import math
def std (lista, avg):
    if isinstance(lista,list) and isinstance (avg, float):
        return mah.sqrt(std_aux(lista, avg)/(len(lista)-1)
    else: return "ERROR"
def std_aux(lista, avg, resultado):
    if lista==[]:
        return 0
    else: return (std_aux(lista[1:], avg,((lista[0]-avg)**2))
