"""
39. Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
"""

mais_alto = 0
mais_baixo = 0

for i in range(1, 4):
    lista = []
    n_aluno = int(input('Informe o número do aluno: '))
    alt_aluno = int(input('Informe a altura do aluno em centímetros: '))
    lista.append({'Aluno': n_aluno, 'Altura': alt_aluno})
    if alt_aluno > mais_alto:
        mais_alto = alt_aluno
    if alt_aluno < mais_alto:
        mais_baixo = alt_aluno

    print(lista)
