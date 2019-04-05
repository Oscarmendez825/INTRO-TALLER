def combinaciones(hp, dell):
    if isinstance (hp, list) and isinstance (dell, list) and len (hp) > 0 and len (dell)>0:
        return combinaciones_aux(hp, dell,[])
    else: return "ERROR"
def combinaciones_aux (hp, dell,resultado):
    if hp == []:
        return resultado
    else: return  combinaciones_aux (hp[1:], dell, resultado + comb_aux(hp[0], dell, []))) 
def comb_aux(valor, dell,resultado):
    if dell==[]:
        return resultado
    else: return comb_aux(valor, dell [1:]+[valor+dell[0]])
    print(combinaciones(hp, dell))
