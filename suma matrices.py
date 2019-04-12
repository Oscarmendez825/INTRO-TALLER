def matriz(m1,m2):
    if isinstance(m1, list) and m1!=[] and isinstance (m2,list) and m2!=[]:
        return sumam1(m1,m2, 0, 0, [],[])
    else: return "VAYA ERROR COMPAÑERO"
def sumam1(m1, m2, f, c, rMat, fila):
    if f == len(m1):
        return rMat
    elif c == len(m1[0]):
        return sumam1(m1,m2, f+1, 0, rMat + [fila], [])
    else: return sumam1(m1,m2,f,c+1, rMat,  fila + [m1[f][c]+m2[f][c]])
m1=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
m2=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print (matriz(m1,m2)) 
