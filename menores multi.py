def multi(factor, num):
    if isinstance(factor,int) and isinstance (num, int):
        return multi_aux(factor, num, 0)
    else: return "EL VALOR NO PUEDE SER CALCULADO"
def multi_aux (factor, num,potencia):
    if num==0:
        return 0
    elif ((num%10)*factor)<=9:
        return (factor*num%10)*(10**potencia)+multi_aux(factor, num//10, potencia+1)
    else:
        return multi_aux(factor, num//10, potencia)
