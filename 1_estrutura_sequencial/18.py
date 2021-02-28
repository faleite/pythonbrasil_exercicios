""" 18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe
o tempo aproximado de download do arquivo usando este link (em minutos). """

tamanho = float(input(f'Informe o tamanho do arquivo para download (em MB): '))
velocidade = float(input(f'Informe a velocidade do link (em Mbps): '))

segundos = tamanho / (velocidade / 8)  # Tempo em segundos (1 byte equivale a 8 bits)
minutos = int(segundos / 60)  # Tempo em minutos

print(f'O tempo aproximado de download é: {minutos} minutos')
