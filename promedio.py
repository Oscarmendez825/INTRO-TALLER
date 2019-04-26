class matriz1(object):
    def _init(self):
        pass
    def matriz(self,m):
        if isinstance(m, list):
            return self.sumam(m, 0, 0, 0)/(len(m)*len(m[0]))
        else: return "VAYA ERROR COMPAÑERO"
    def sumam(self,m, f, c, resultado):
        if f == len(m):
            return resultado
        elif c == len(m[0]):
            return self.sumam(m, f+1, 0, resultado)
        else: return self.sumam(m,f,c+1, resultado + m[f][c])
