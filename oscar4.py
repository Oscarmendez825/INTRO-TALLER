#Entrada: es un número entero
#Restricciones: es un entero positivo mayor a cero
#Salida: suma de los dígitos
def calcular(num,x):
    if(isinstance(num, int) and (num >0) and isinstance(x, int) and (x>=0)):
        return calcular_aux(num,x)
    else:
        return "Error"
def calcular_aux(num, x)
    if(num == 0):
        return 0
    elif(num % 10 == x)
        return 1 + calcular_aux (num //10, d)
    else:
        return: calcular_aux(num//10, d)
    
