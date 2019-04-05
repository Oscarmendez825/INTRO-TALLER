def pares(num):
    if isinstance(num, int):
        return pares_aux(num)
    else:
        return "Error"
def pares_aux(num):
    if num == 0:
        return 0
    elif (num % 10):
        if (num %10 >=0 and num % 10 <=4):
            return "True"
        else:
            return "False"
    else:
        return 0

