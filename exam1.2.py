def pares(num):
    if isinstance(num,int)and(num>0):
        return pares_aux(num)
    else: return "ERROR"
def pares_aux (num):
    if num==0:
        return 0
    elif (num>0 and (num%10)%2==0):
        return [num[0]+[pares_aux(num%10)%2]]
    else: return pares_aux(num%10)
