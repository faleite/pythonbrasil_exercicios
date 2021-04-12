"""
16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
"""

ntermos = int(input('Insira um número: '))

n1 = 0
n2 = 1
termo = 0

count = 0

while count < ntermos:
	termo = n1 + n2
	n1 = n2
	n2 = termo
	count += 1
if termo < 500:
	print('Tente novamente')
else:
	print(termo)
	