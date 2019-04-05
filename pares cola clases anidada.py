#lista anidada y pares
class pares2(object):
    def _init_(self):
        pass
    def pares(self,lista):
        cond = lambda lista:lista%2==0
        if isinstance (lista, list) and lista != []:
            return self.pares_aux(lista, [], cond)
        else: return "ERROR"
    def pares_aux(self,lista, resultado, cond):
        if lista==[]:
            return resultado
        elif isinstance(lista[0], list):
            return ((self.pares_aux(lista[0]+lista[1:], resultado, cond)))
        elif cond(lista[0]):
            return self.pares_aux(lista[1:], resultado + [lista[0]] , cond)
        else: return self.pares_aux(lista[1:], resultado , cond)
