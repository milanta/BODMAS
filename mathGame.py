try:
	import PythonFunctions as p
	userName = input('Nombre de usuario: ')
	userScore = int(p.getUserPoint(userName))
	if userScore == -1:
		newUser = True
		userScore = 0
	else:
		newUser = False
	userChoice = 0
	while userChoice != 'exit':
		userScore += p.Questions()
		print('Puntaje actual: ',userScore)
		userChoice = input('Enter para continuar o exit para salir: ') 
	p.updateUserPoints(newUser,userName,str(userScore))

except Exception as e:
	print('Error',e)
