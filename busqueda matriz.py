class busqueda(object):
    def _init_(self):
        pass
    def busq(self, matriz, elemento):
        if isinstance (matriz, list) and matriz !=[]:
            return self.busq_aux(matriz,elemento, 0, 0)
        else: return "error"
    def busq_aux(self, matriz, elemento,f,c):
        if f==len(matriz):
            return False
        elif c == len(matriz[0]):
            return self.busq_aux(matriz, elemento,f+1,0)
        elif elemento == (matriz[f][c]):
            return True
        else:return self.busq_aux(matriz, elemento, f, c+1)
