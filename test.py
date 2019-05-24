from clasepila import Pila
class Prueba2:
    def __init__(self):
        self.__pila=Pila()
    def test2(self,numero):
       while numero > 0:
           self.__pila.push(num%10)
           numero//=10

    def test3(self):
        res = 0
        cont = 0
        while not self.__pila.is_empty():
            res += self.__pila.pop() * 10 ** cont
            cont +=1
        return res
    def ejecutar(self,numero):
        self.test2(self,numero)
        return self.test3()
        
