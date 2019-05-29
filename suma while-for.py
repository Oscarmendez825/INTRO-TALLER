def sumawhile(lista):
	resultado = 0
	contador = 0
	largo = len(lista)
	while contador < largo:
		resultado += lista[contador]
		contador += 1
	return resultado

def sumaslicing(lista):
	resultado = 0 
	while lista != []:
		resultado += lista[0]
		lista =lista[1:]
	return resultado

def sumafor(lista):
	resultado = 0
	for contador in range (len(lista)):
		resultado += lista[contador]
	return resultado
def sumafor2(lista):
	resultado = 0
	for valor in lista:
		resultado += valor
	return resultado