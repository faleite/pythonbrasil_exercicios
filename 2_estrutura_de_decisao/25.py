"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print('Responda as perguntas com 1-Sim ou 0-Não.')
a = int(input(f'Telefonou para a vítima? '))
b = int(input(f'Esteve no local do crime? '))
c = int(input(f'Mora perto da vítima? '))
d = int(input(f'Devia para a vítima? '))
e = int(input(f'Já trabalhou com a vítima? '))

respostas = a + b + c + d + e

if respostas == 2:
    print('Suspeita')
elif 3 <= respostas <= 4:
    print('Cúmplice')
elif respostas == 5:
    print('Assassino')
else:
    print('Inocente')
