#recursion de cola
def largo(num):
    if isinstance (num, int):
        return largo_aux(num, 0)
    else: return "ERROR"
def largo_aux(num, resultado):
    print(resultado, end=" -- ")
    if (num==0):
        return resultado
    else: return largo_aux(num//10, resultado + 1)
