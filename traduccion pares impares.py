def pares(num):
    resultado1=[]
    resultado2=[]
    while num>0:
        digi = num % 10
        if digi%2==0:
            resultado1+=[digi]
        else: resultado2+=[digi]
        num = num//10
    print(resultado1,resultado2)


    
def newnum(num):
    resultado = 0
    contador = 0
    while num>0:
        digito = num % 10
        if digito%2 == 0:
            resultado += (digito)*10**contador
            contador += 1
        num//=10
    print(resultado)


def nuevoimp(num):
    resultado = 0
    resultado2 = 0
    contador1 = 0
    contador2 = 0
    while num>0:
        digito = num % 10
        if digito%2 == 0:
            resultado += (digito)*10**contador1
            contador1 += 1
        else:
            resultado2 += (digito)*10**contador2
            contador2 += 1
        num//=10
    print(resultado,resultado2)
