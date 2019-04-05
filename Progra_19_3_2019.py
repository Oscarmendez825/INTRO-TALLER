#Calculo de Factorial

def fact_aux(Num,FactNum):
    if Num == 1:
        return FactNum
    else:
        FactNum = Num*FactNum
        return fact_aux(Num -1,FactNum)

def fact(Num):
    if isinstance (Num,int):
        if Num == 1 or Num == 0:
            return 1
        else:
            return fact_aux(Num,1)
    else:
        return 'Debe ser un numero entero'

#Sucesion Fibonacci

def fib(Num):
    if isinstance (Num,int):
        if Num >= 0:
            return fib_aux(Num,1,1,1)
        else:
            return 'Num, debe ser >=0'
    else:
        return 'Error Num, debe ser tipo entero'

def fib_aux(Num,Cont,F1,F2):
    if Num == Cont:
        return F2
    else:
        Cont=Cont+1
        return fib_aux(Num,Cont,F2,F1 + F2)
