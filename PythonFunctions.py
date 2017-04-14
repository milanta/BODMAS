from random import randint
from os import remove, rename

def getUserPoint(arg):
	try:
		o = open('userScores.txt','r')
		for line in o:
			content = line.split(',')
			if arg == content[0]:
				o.close()
				return content[1]
		o.close()
		return '-1'
	
	except IOError:
		print('i\n File not found, creating it :D')
		input = open('userScores.txt','w')
		input.close()
		return '-1'

def updateUserPoints(newUser,userName,score):
	if newUser:
		o = open('userScores.txt','a')
		o.write(userName + ', ' + score)
		o.write('\n')
		o.close()
	else:
		output = open('userScores.tmp','w')
		input = open('userScores.txt','r')
		for line in input:
			content = line.split(',')
			if content[0] == userName:
				content[1] = score
			line = content[0] + ', ' + content[1] + '\n'
			output.write(line)
		input.close()
		output.close()
		remove('userScores.txt')
		rename('userScores.tmp','userScores.txt')	


def Questions():
	operandList = [0,1,2,3,4]
	operatorList = ['','','','']
	operatorDict = {1:'+',2:'-',3:'*',4:'**'}

	ol = []
	for x in operandList:
        	x = randint(1,9)
        	ol.append(x)
	operandList = ol
	op = []
	for x in operatorList:
        	rand = randint(1,4)
        	value = operatorDict[rand]
        	op.append(value)
	p = ['**', '**']
	while op[0:2] == p  or op[1:3] == p or op[2:4] == p:
        	op = []
        	for x in operatorList:
                	rand = randint(1,4)
                	value = operatorDict[rand]
                	op.append(value)
        	continue
	operatorList = op

	questionString = ''.join([str(a) + str(b) for a,b in zip(ol,op)]) + str(ol[-1])
	result = eval(questionString)
	questionString = questionString.replace("**", "^")
	print('Cual es el resultado de: ',questionString)
	while 1:
		try:
			respuesta = int(input('Respuesta: '))
			if result == respuesta:
				print('Respuesta Correcta!')
				return 1
			else:
				print('Respuesta incorrecta, la respuesta correcta es', result)
				return 0
		except Exception as e:
			print('Error',e)

#que = questionString[1:16:3]
#question = []
#count = 0
#for x in op:
#	y = que[count] + x
#	question.append(y)
#	count = count +1
#
#final = ''.join(question)
#final1 = final[0:-1]
#print(final1)
#print(final)
