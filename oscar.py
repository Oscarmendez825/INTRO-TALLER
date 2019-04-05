def cuenta_regresiva(i):
	print(i, end=" ")
	if(i<=1):
		return
	else: cuenta_regresiva(i-1)
