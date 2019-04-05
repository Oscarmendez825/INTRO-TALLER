#pares impares con lambda
def par_impar(lista):
    if isinstance (lista, list):
        impar = lambda digito : digito % 2 == 1
        par = lambda digito : digito %2 == 0
        return(par_impar_aux(lista, par), par_impar_aux(lista, impar))
    else: return "El valor ingresado no es una lista"

def par_impar_aux(lista, condicion):
    if lista == []:
        return []
    elif condicion(lista [0]):
        return [lista [0]] + par_impar_aux(lista [1:], condicion)
    else: return par_impar_aux(lista[1:], condicion)                  
 
