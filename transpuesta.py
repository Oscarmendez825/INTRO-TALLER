class transpuesta(object):
    def _init_ (self):
        pass
    def matriz(self, matriz):
        if isinstance(matriz,list) and matriz !=[]:
            return self.matriz_aux(matriz, 0,0,[],[])
        else:return "error"
    def matriz_aux(self, matriz, f,c, resultado,fila):
        if c==len(matriz[0]):
            return resultado
        elif f== len (matriz):
            return self.matriz_aux(matriz,0,c+1, resultado + [fila],[])
        else: return self.matriz_aux(matriz, f+1,c, resultado, fila + [matriz[f][c]])
                   
