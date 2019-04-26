class matriz1(object):
    def _init(self):
        pass
    def matriz(self,n,m):
        if isinstance(n,int) and isinstance (m, int) :
            return self.change(n,m,[],[],[],0,0)
        else: return "VAYA ERROR COMPAÑERO"
    def change (n,m,matriz,fila,columna,indicefila,indicecolumna):
        if indicefila==n and indicecolumna==m:
            return matriz
        elif indicecolumna == m:
            return self.change(n,m,matriz+[fila],[columna],indicefila+1,0)
        elif indicefila == n:
            return self.change(n,m,matriz+[fila],[columna],indicefila,indicecolumna+1)
