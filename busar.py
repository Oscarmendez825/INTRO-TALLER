class encontrar(object):
    def __int__(self):
        pass
    def busqueda_1(self,matriz):
        if isinstance(matriz, list)and len(matriz)==len(matriz[0]):
            return self.seguido(matriz,1)
        else: return "Error"
    def seguido(self,matriz,num):
        if num >(len(matriz)*len(matriz[0])):
            return True
        elif (self.buscar(num,matriz,0,0)):
            return self.seguido(matriz, num+1)
        else: return False
                
    def buscar(self, elemento, matriz, f,c):
        if len(matriz) == f:
            return False
        elif c == len(matriz[0]):
            return self.buscar(elemento,matriz, f+1, 0)
        elif matriz[f][c]==elemento:
            return True
        else: return self.buscar(elemento,matriz,f,c+1)
        
c=encontrar()
print(c.busqueda_1([[3,2],[1,4]]))


 
