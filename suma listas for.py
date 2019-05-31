class suma(object):
    def __init__ (self):
        pass
    def sumalistas(self,lista1,lista2):
        if len(lista1) == len (lista2):
            resultado = 0
            for indice in range (len (lista1)):
                resultado += lista1[indice] + lista2[indice]
            return resultado
        else: return "Error"
    #crear una nueva lista
    def nuevalista(self, lista1,lista2):
        if len(lista1) == len (lista2):
            resul = []
            for indice in range (len(lista1)):
                resul += [lista1[indice] + lista2[indice]]
            return resul
        else: return "Error"
        
    def matriz(self, m1,m2):
        if len(m1) == len (m2):
            suma1 = []
            for indice1 in range (len(m1)):
                fil = []
                for indice2 in range (len(m1[0])):
                    fil += [m1[indice1][indice2] + m2[indice1][indice2]]
                suma1+=[fil]
            return suma1
        else: return "Error"
    def trans(self,m1):
        suma1 = []
        for c in range (len(m1[0])):
            fil = []
            for f in range (len(m1)):
                fil += [m1[f][c]]
            suma1+=[fil]
        return suma1
    def diagonal(self,m1):
        
        suma1 = 0
        for fc in range (len(m1)):
            suma1 += m1[fc][fc]
        return suma1
    def asteriscos(self,n,m):
        mtz = []
        for f in range (n):
            resultado = []
            for c in range (m):
                if f == 0 or f == (n-1):
                    resultado += ["*"]
                elif c == 0 or c == (m-1):
                    resultado+=["*"]
                else:
                    resultado+=["0"]
            mtz +=[resultado]
        return mtz
    def asteriscos2(self,num):
        lado = (num * 2)-1
        mitad = lado//2
        lado1iz = mitad
        lado2de = mitad 
        
        mtx = []
        for f in range (0, lado , 2):
            resultado = []
            for c in range (lado):
                if fila = 0 and columna == mitad:
                    print("*", end = " ")
                elif columna == ladoiz or  columna == ladoder or (fila == lado-1 and columna % 2 == 0):
                    print ("*", end = " ")
                
                         
             
    


