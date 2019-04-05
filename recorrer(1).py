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
        else:self.recorrer_aux(lista, resultado, lista[indice], indice+1)
