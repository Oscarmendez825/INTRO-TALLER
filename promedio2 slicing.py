class matriz1(object):
    def _init(self):
        pass
    def matriz(self,m):
        if isinstance(m, list):
            return self.prom(m,0)/(len(m)*len(m[0]))
        else: return "VAYA ERROR COMPAÑERO"
    def prom(self,m,resultado):
        if m==[]:
            return resultado
        elif isinstance(m[0],list):
            return self.prom(m[0]+m[1:],resultado)
        else: return self.prom(m[1:],resultado+m[0])
            
        
