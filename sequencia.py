from random import sample
ordem= str(input("Digite aqui o nome dos alunos:")).split(",")
print(f"Diante dos alunos informados, a ordem de apresentação do trabalho será {sample(ordem, 4)}")

'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

'''

