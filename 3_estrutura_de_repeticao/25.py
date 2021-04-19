"""
25. Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade
da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer
se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

pessoas = int(input('Insira o número de pessoas: '))

soma = 0
media = 0

for i in range(1, pessoas + 1):
    idade = int(input(f'Insira a idadde da {i}ª pessoa: '))
    soma += idade
    media = soma / pessoas

if media <= 25:
    print('A turma é Jovem')
elif 25 < media <= 60:
    print('A turma é adulta')
else:
    print('A turma é idosa')
