class recorridos(object):
    def _init_(self):
        pass
    def recorrer(self, lista):
        if isinstance(lista,list):
            return self.recorrer_aux(lista,0,0)
        else: return "error"

    def recorrer_aux(self,lista, resultado, indice):
        if indice == len(lista):
            return resultado
        elif (lista[indice]>resultado):
            return self.recorrer_aux(lista, lista[indice], indice+1)
        else: return self.recorrer_aux(lista, resultado, indice+1)
#lista = [5,[6,[7,8],9,10],11]
lista=[5,6,7,8,9,10,11]
r=recorridos()
print(r.recorrer(lista))
