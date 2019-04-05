def zScore(lista, avg,s):
    if (isinstance(lista,list) and type (avg) ==float and type(s)==float):
        return zScore_aux(lista, avg, s)
    else: return "ERROR"
def zScore_aux(lista, avg, s):
    if lista==[]:
        return[]
    else:return [(lista[0]-avg)-avg/s]+zScore_aux(lista[1:], avg, s)
print(zScore(x,185.75,2.87)
#------------------------------cola--------------------------------------#
def zScore(lista, avg,s):
    if (isinstance(lista,list) and type (avg) ==float and type(s)==float):
        return zScore_aux(lista, avg, s,[])
    else: return "ERROR"
def zScore_aux(lista, avg, s, resultado):
    if lista==[]:
        return resultado
    else:return zScore_aux(lista[1:], avg, s,resultado+[(lista[0]-avg)-avg/s])
print(zScore(x,185.75,2.87)
