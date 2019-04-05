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

#Cont Numero flotante a uno entero



#Lista par, lista impar

def par_imp_aux(Lista,Ind,Cant,ListaPar,Listaimpar):
    if Cant == Ind:
        return Lista,ListaPar,ListaImpar
    else:
        if Lista(Ind)%2 == 1:
            ListaImpar = ListaImpar + [Lista[Ind]]
            Ind = Ind + 1
            return par_impar_aux(Lista,Ind,Cant,ListaPar,ListaImpar)
        else:
            ListaPar == ListaPar + [Lista[Ind]]
            Ind = Ind + 1
            return par_impar_aux(Lista,Ind,Cant,ListaPar,ListaImpar)


#Ejercicios #1 Jueces

def mayor_aux(Puntajes, Result):
    if Lista == []:
        return Result
    elif Lista [0] > Result:
        return mayor_aux(Lista[1:], Lista[0])
    else:
        return mayor_aux(Lista[1:],Result)

def menor_aux(Puntajes, Result1):
    if Lista == []:
        return Result1
    elif Lista [0] < Result1:
        return menor_aux(Lista[1:], Lista[0])
    else:
        return menor_aux(Lista[1:], Lista[0])
    
def evaluacion(Puntajes, Result):
    if isinstance(Puntajes,list):
        return mayor_aux(Puntajes, Result), menor_aux(Puntajes, Result1)

    
