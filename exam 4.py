def rScore(Sx,Sy):
    if (isinstance(Sx,list) and isinstance(Sx,list) and len(Sx)==len(Sy)):
        return rScore_aux(Sx,Sy)/(len(Sx)-1)
    else: return "ERROR"
def zScore_aux(lista, avg, s):
    if lista==[]:
        return 0
    else:return (Sx[0]*Sy[0])+rScore_aux(Sx[1:],Sy[1:])
print(rScore(Sx, Sy))
#--------------------------Cola--------------------------------------------#
def rScore(Sx,Sy):
    if (isinstance(Sx,list) and isinstance(Sx,list) and len(Sx)==len(Sy)):
        return rScore_aux(Sx,Sy, 0)/(len(Sx)-1)
    else: return "ERROR"
def zScore_aux(lista, avg, s, resultado):
    if lista==[]:
        return 0
    else:return rScore_aux(Sx[1:],Sy[1:],resultado+(Sx[0]*Sy[0]))
print(rScore(Sx, Sy))
