"""
45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão
e ao final comparar com o gabarito da prova e assim calcular o total de acertos
e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor
digite o gabarito da prova antes dos alunos usarem o programa.
"""

resp = ''
for r in range(1, 11):
    resposta = str(input(f'Informe a resposta da {r}ª questão: ')).upper()
    resp += resposta
print('-='*30)

maior = menor = total = total_acertos = 0

while True:
    acertos = 0
    for i in range(1, 11):
        questao = str(input(f'Informe a alternativa correta da {i}ª questão: ')).upper()
        if i == 1:
            if questao == resp[0]:
                acertos += 1
        if i == 2:
            if questao == resp[1]:
                acertos += 1
        if i == 3:
            if questao == resp[2]:
                acertos += 1
        if i == 4:
            if questao == resp[3]:
                acertos += 1
        if i == 5:
            if questao == resp[4]:
                acertos += 1
        if i == 6:
            if questao == resp[5]:
                acertos += 1
        if i == 7:
            if questao == resp[6]:
                acertos += 1
        if i == 8:
            if questao == resp[7]:
                acertos += 1
        if i == 9:
            if questao == resp[8]:
                acertos += 1
        if i == 10:
            if questao == resp[9]:
                acertos += 1

    if acertos > maior:
        maior = acertos
    if acertos < maior or acertos == 1:
        menor = acertos
    total += 1
    total_acertos += acertos
    print(f'Total de acertos e a nota: {acertos}')
    print('0utro aluno vai utilizar o sistema?')
    proximo = str(input('Digite S para sim ou N para não: ')).upper()
    if proximo == 'N':
        break

print('-='*30)
print(f'Maior Acerto: {maior}')
print(f'Menor Acerto: {menor}')
print(f'Total de Alunos que utilizaram o sistema: {total}')
print(f'Média das Notas da Turma: {total_acertos/total:.2f}')
