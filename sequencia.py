from random import sample
alunos= str(input('Digite aqui o nome dos alunos participantes:')).strip().split()
print(f'Referente ao nome dos alunos, a ordem de apresentação será {sample(alunos, 3)}')

'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

'''

