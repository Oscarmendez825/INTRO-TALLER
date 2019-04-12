def matriz(m):
    if isinstance(m, list):
        return sumam(m, 0, 0, 0)
    else: return "VAYA ERROR COMPAÑERO"
def sumam(m, f, c, resultado):
    if f == len(m):
        return resultado
    elif c == len(m[0]):
        return sumam(m, f+1, 0, resultado)
    else: return sumam(m,f,c+1, resultado + m[f][c])
