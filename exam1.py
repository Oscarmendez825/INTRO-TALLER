def combinaciones(hp, dell):
    if isinstance (hp, list) and isinstance (dell, list) and len (hp) > 0 and len (dell)>0:
        return combinaciones_aux(hp, dell)
    else: return "ERROR"
def combinaciones_aux (hp, dell):
    if hp == []:
        return[]
    else: return comb _aux(hp[0], dell) + combinaciones_aux (hp[1:], dell)
def com_aux(valor, dell):
    if dell==[]:
        return []
    else: return [valor+dell[0]]+com_aux(valor, dell [1:])
