def busca_bin(Lista, Ele):
    return busca_bin_aux(Lista, Ele, Ini,Fin)
def busca_bin_aux(Lista, Ele, Ini, Fin):
    if Fin<Ini:
        return False
    mitad = (Ini+Fin)//2
    if Lista[Mitad]>Ele:
        return busca_bin_aux(Lista, Ele, Ini, Mitad-1)
    elif Lista[Mitad]<Ele:
        return busca_bin_aux(Lista, Ele, Mitad+1, Fin)
    else:
        return Mitad

def burbuja(Lista):
    return burbuja_aux(Lista, 0,0,len(Lista), False)
def burbuja_aux(Lista, i, j, n, Swap):
    if i==n:
        return Lista
    if j==n-i-1:
        if Swap:
            return burbuja_aux(Lista, i+1,0,n, False)
        else:
            return Lista
    if Lista[j]>Lista[j+1]:
        Temporal=Lista[j]
        Lista[j]=Lista[j+1]
        Lista[j+1]=Temporal
        return burbuja_aux(Lista, i, j+1, n, True)
    else:
        return burbuja_aux(Lista, i, j+1, n, Swap)
##### Se Obtiene el menor de una lista
    

def seleccion(Lista):
    return seleccion_aux(Lista, 0,len(Lista))
def menor(Lista,j,n,Min):
    if j==n:
        return Min
    if Lista[j]<Lista[Min]:
        Min=j
    return menor(Lista, j+1, n, Min)
def seleccion_aux(Lista, i, n):
    if i==n:
        return Lista
    Min=menor(Lista, i+1,n,i)
    Tmp=Lista[i]
    Lista[i]= Lista[Min]
    Lista[Min]=Tmp
    return seleccion_aux(Lista, i+1,n)
#Ordenamiento por insercion
def insert_sort(Lista):
    return insert_sort_aux(Lista, 1, len(Lista))
def insert_sort_aux(Lista, i, n):
    if i==n:
        return Lista
    Aux=Lista[i]
    j=incluye_orden(Lista, i, Aux)
    Lista[j]=Aux
    return insert_sort_aux(Lista, i+1, n)
def incluye_orden(Lista,j, Aux):
    if j<=0 or Lista[j-1]<=Aux:
        return j
    Lista[j]=Lista[j-1]
    return incluye_orden(Lista, j-1, Aux)
#QuickSort, Algoritmo de ordenamiento rapido, se escoge un pivote
def quick_sort(Lista):
    Iguales=[]
    Menores=[]
    Mayores=[]
    if len(Lista)<=1:
        return Lista
    Pivote=Lista[-1]
    partir(Lista, 0, len(Lista), Pivote, Menores, Iguales, Mayores)
    Ret=quick_sort(Menores)
    Ret.extend(Iguales)
    Ret.extend(quick_sort(Mayores))
    return Ret
def partir(Lista, i, n, Pivote, Menores, Iguales, Mayores):
    if i==n:
        return Menores, Iguales, Mayores
    if Lista[i]<Pivote:
        Menores.append(Lista[i])
    elif Lista[i]>Pivote:
        Mayores.append(Lista[i])
    elif Lista[i]==Pivote:
        Iguales.append(Lista[i])
    return partir(Lista, i+1, n, Pivote, Menores, Iguales, Mayores)
#N numeros random de dos dígitos
import random
def ran_dig(N):
    return ran_dig_aux([], N, 0)
def ran_dig_aux(Lista, N, Num):
    if N==Num:
        return Lista
    else:
        Lista.append(random.randint(10,99))
        return ran_dig_aux(Lista, N, Num+1)
# Construir una funcion que retorne el valor promedio de los elementos de una tupla.
def prom_tupla(Valor):
    if isinstance(Valor, list) or isinstance(Valor, tuple):
        return prom_tupla_aux(Valor, len(Valor), 0, 0)
    else:
        return "No es ni una tupla ni una lista"
def prom_tupla_aux(Valor, N, Len, Suma):
    if Valor==() or Valor==[]:
        promedio=Suma/(Len)
        return promedio
    else:
        Suma=Suma+Valor[0]
        return prom_tupla_aux(Valor[1:], N, Len+1, Suma)
        
    


    
    




    
    
