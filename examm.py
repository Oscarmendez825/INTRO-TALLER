def cadena(letras):
    if isinstance(letras, str):
        return cadena_aux(letras, 0)
    else: return "error"
def cadena_aux (letras,dig):
    if letras== "":
        return 0
    elif (letras [0] == 'a'or letras[0] =='e' or letras[0]=='i'or letras[0]=='o' or letras[0] =='u'):
        return cadena_aux(letras[1:], dig)
    else: return (dig+1)+ cadena_aux(letras[1:],dig)
