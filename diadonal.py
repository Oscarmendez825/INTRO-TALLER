#Sumar en diagonal una matriz NXN
class matriz1(object):
    def _init_(self):
        pass
    def diagonal(self,matriz):
        if isinstance (matriz, list) and matriz !=[]:
            return self.diagonal_aux(matriz,0,0)
        else: return "ERROR"
    def diagonal_aux(self,matriz,fc, resultado):
        if fc == len(matriz):
            return resultado
        else: return self.diagonal_aux(matriz,fc+1,resultado+matriz[fc][fc])
