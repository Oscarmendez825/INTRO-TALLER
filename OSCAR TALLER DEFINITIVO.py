NUMEROS={
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G"
}
class sumas_bases(object):
    def _init_(self):
        pass
    def lasumabases(self, num1,num2,base,acarreo):
        if (isinstance(num1, list) and(num2, list) and (base,int) and (acarreo,int)
            and len(num1)==len(num2)):
            return self.lasumabases_aux(num1,num2,base,acarreo)
        else:
            return "FATAL ERROR"
    def lasumabases_aux(self,num1,num2,base,acarreo):
        if num1==[] and num2==[] and acarreo>=0 and base>=0:
            return [acarreo]
        elif (num1[-1]+num2[-1]+acarreo)>base:
            return self.lasumabases(num1[:-1],num2[:-1],base,1)+([(num1[-1]+num2[-1]+acarreo)%base])
        elif (num1[-1]+num2[-1]+acarreo)==base:
            return self.lasumabases(num1[:-1],num2[:-1],base,1)+[0]
        else:
            return self.lasumabases(num1[:-1],num2[:-1],base,0)+[num1[-1]+num2[-1]+acarreo]


#OSCAR MENDEZG
