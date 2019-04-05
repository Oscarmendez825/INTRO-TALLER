#hacer una funcion que reciba una lista y obtenga otra lista con los numeros pares. utilice slicing
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
        elif cond(lista[0]):
            return self.pares_aux(lista[1:], resultado + [lista[0]] , cond)
        else: return self.pares_aux(lista[1:], resultado , cond)
