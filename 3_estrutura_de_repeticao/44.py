"""
44. Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
- O total de votos para cada candidato;
- O total de votos nulos;
- O total de votos em branco;
- A percentagem de votos nulos sobre o total de votos;
- A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
"""
print('Tabela de códigos para votação:')
print('1 - Jose\n2 - João\n3 - Maria\n4 - Pedro\n5 - Voto Nulo\n6 - Voto em Branco')

c1 = c2 = c3 = c4 = c5 = c6 = 0
total_votos = 0

while True:
    votos = int(input('Informe código para votar ou digite 0 para finalizar: '))
    if votos == 0:
        break

    if votos == 1:
        c1 += 1
    if votos == 2:
        c2 += 1
    if votos == 3:
        c3 += 1
    if votos == 4:
        c4 += 1
    if votos == 5:
        c5 += 1
    if votos == 6:
        c6 += 1
    total_votos += 1

print(total_votos)
print(f'Total de votos para o cadidato Jose: {c1}')
print(f'Total de votos para o cadidato João: {c2}')
print(f'Total de votos para o cadidato Maria: {c3}')
print(f'Total de votos para o cadidato Pedro: {c4}')
print(f'Total de votos Nulos: {c5}')
print(f'Total de votos em Branco: {c6}')
print(f'Percentagem de votos nulos: {c5 / (total_votos / 100):.2f}%')
print(f'Percentagem de votos em branco: {c6 / (total_votos / 100):.2f}%')
