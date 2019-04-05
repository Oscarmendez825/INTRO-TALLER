###Ejercicio 2: Programe una funcion que compruebe que
###un numero entero es un palindromo.

def palindromo(num):
    if isinstance (num, int) and num > 0: 
        return pal_aux(num, num, contar(num, 0))
    else: return "El valor ingresado nu cumple con las condiciones"
def pal_aux(num,num1, n):
    if num == 0:
        return True
    if num%10 == (num1//(10**(n-1))):
        return pal_aux(num//10, num1%10**(n-1), n-1)
    else: return False
def contar(num, contador):
    if num == 0:
        return 0
    if num > 0:
        return (contador + 1) + contar(num//10, contador)
    else: return
