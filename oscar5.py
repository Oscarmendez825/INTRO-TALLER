#Entrada: es un número entero
#Restricciones: es un entero positivo mayor a cero
#Salida: suma de los dígitos
def calcular(num):
    if(isinstance(num, int) and (num >0) and isinstance(x, int) and (x>=0)):
        return calcular_aux(num,x)
    else:
        return "Error"
def calcular_aux(num):
    if(num == 0):
        return 0
    elif((num % 10 == x)% 2 == 0):
        return 1 + calcular_aux(num //10)
    else:
        return calcular_aux(num//10)
    
