class voltear(object):
    def _init_(self):
        pass
    def pasar(self, lista):
        if isinstance (lista, list):
            return self.pasar2(lista,0,len(lista)-1)
        else: return "ERROR"

    def pasar2(self,lista,indice1, indice2):
        if indice1-1==indice2:
            return lista
        else:
            lista[indice1],lista[indice2]=lista[indice2],lista[indice1]
            return self.pasar2(lista, indice1+1, indice2-1)
lista=[0,1,2,3,4,5,6,7,8,9]
vo=voltear()
print(vo.pasar(lista))
