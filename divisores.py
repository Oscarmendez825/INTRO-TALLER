def divisores(num):
    if isinstance (num, int):
        if num == 0 or num ==1:
            return []
        else:
            return divisores_aux(num,2)
def divisores_aux (num, div):
    if div == num:
        return []
    elif num%div==0:
        return [div]+divisores_aux(num, div +1)
    else: return divisores_aux(num, div+1)
