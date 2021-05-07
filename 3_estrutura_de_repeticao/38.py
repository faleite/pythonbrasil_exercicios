"""
38. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário
digite o salário inicial do funcionário.
"""

salario = float(input('Informe o salário inicial do funcionário: '))
ano_inicio = int(input('Informe a data de inicio: '))
ano_atual = int(input('Informe a data atual: '))

aumento = 1.5


for n in range(ano_inicio, ano_atual):
    salario += (salario * aumento) / 100
    aumento *= 2

print(f'Salário atual = R$ {salario:.2f}')




