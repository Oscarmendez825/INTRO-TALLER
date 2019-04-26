class matriz1(object):
    def _init(self):
        pass
    def matriz(self,m):
        if isinstance(m, list):
            return self.sumam(m, 0, 0)
        else: return "VAYA ERROR COMPAÑERO"
    def sumam(self,m, f, c):
        if f == len(m):
            return m
        elif c == len(m[0]):
            return self.sumam(m,f+1,0)
        elif f == 0 or f == (len(m)-1)or c == 0 or c == (len(m[0])-1):
            m[f][c] = '*'
            return self.sumam(m,f,c+1)
        else:return (self.sumam(m,f,c+1))
        
ma=matriz1()
m = ma.matriz([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
print(ma.matriz(m))
