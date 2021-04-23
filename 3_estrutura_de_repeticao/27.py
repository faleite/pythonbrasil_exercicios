"""
27. Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

turma = int(input('Insira a quantidade de turmas: '))

som_alun = 0
media = 0

for i in range(1, turma + 1):
    while True:
        alunos = int(input(f'Insira a quantidade de alunos da {i}ª turma: '))
        if alunos <= 40:
            break
        else:
            print('As turmas não podem ter mais de 40 alunos.')
            print('Tente novamente.')
    som_alun += alunos
    media = som_alun / turma

print(f'O número médio de alunos por turma é: {media:.2f}')
