def voltear(num):
    if isinstance(num, int):
        return voltear_aux(num,1)
    else:return "HAS COMETIDO UN GRAVE ERROR"
def voltear_aux(num, exp):
    if num==0:
        return 0
    else: return (num//100*10**exp)+(num//10*10**exp) + voltear_aux(num*10**exp+1)
