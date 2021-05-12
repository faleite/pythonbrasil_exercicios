"""
39. Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
"""

mais_alto = mais_baixo = 0
lista = []

for i in range(1, 4):
    n_aluno = int(input('Informe o número do aluno: '))
    alt_aluno = int(input('Informe a altura do aluno em centímetros: '))
    lista.append({'Aluno': n_aluno, 'Altura': alt_aluno})

for y in lista:
    if y['Altura'] > mais_alto:
        a_alto = y['Aluno']
        mais_alto = y['Altura']
    if y['Altura'] < mais_alto:
        a_baixo = y['Aluno']
        mais_baixo = y['Altura']

print('Aluno mais alto:')
print(f'Aluno: {a_alto}, Altura: {mais_alto} cm')

print('Aluno mais baixo:')
print(f'Aluno: {a_baixo}, Altura: {mais_baixo} cm')
