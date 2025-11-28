from random import choice
alunos= str(input('Digite aqui o nome dos alunos participantes:')).strip().split()
print(f'Referente aos alunos informados o ganhador foi {choice(alunos)}!')


'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''