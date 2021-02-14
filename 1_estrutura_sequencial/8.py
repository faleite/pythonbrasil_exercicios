""" 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

valor = float(input('Insira o valor de ganho por hora trabalhada: '))
horas = float(input('Insira o número de horas trabalhadas no mês: '))
salario = valor * horas
print(f'O valor total do seu salario é: $ {salario:.2f}')