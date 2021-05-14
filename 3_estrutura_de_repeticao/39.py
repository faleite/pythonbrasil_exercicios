"""
39. Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
"""

mais_alto = mais_baixo = 0
num_a = num_b = 0

for i in range(1, 4):
    n_aluno = int(input('Informe o número do aluno: '))
    alt_aluno = int(input('Informe a altura do aluno em centímetros: '))

    if i == 1:
        numero = n_aluno
        altura = alt_aluno
    if alt_aluno > altura:
        num_a = n_aluno
        mais_alto = alt_aluno
    if alt_aluno < altura:
        num_b = n_aluno
        mais_baixo = alt_aluno


print('Aluno mais alto:')
print(f'Aluno: {num_a}, Altura: {mais_alto} cm')

print('Aluno mais baixo:')
print(f'Aluno: {num_b}, Altura: {mais_baixo} cm')

""" Outra forma """
# mais_alto = mais_baixo = 0
# lista = []
#
# for i in range(1, 11):
#     n_aluno = int(input('Informe o número do aluno: '))
#     alt_aluno = int(input('Informe a altura do aluno em centímetros: '))
#     lista.append({'Aluno': n_aluno, 'Altura': alt_aluno})
#
# for y in lista:
#     if y['Altura'] > mais_alto:
#         a_alto = y['Aluno']
#         mais_alto = y['Altura']
#     if y['Altura'] < mais_alto:
#         a_baixo = y['Aluno']
#         mais_baixo = y['Altura']
#
# print('Aluno mais alto:')
# print(f'Aluno: {a_alto}, Altura: {mais_alto} cm')
#
# print('Aluno mais baixo:')
# print(f'Aluno: {a_baixo}, Altura: {mais_baixo} cm')
