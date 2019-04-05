def suma_digitos(num):
    if(num == 0):
        return 0
    else:
        return num % 10 + suma_digitos(num//10)
