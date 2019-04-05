
def secuencia(n):
    if (n <= 1):
        return 1
    else:
       return secuencia(n - 1) + secuencia(n -2)
    

