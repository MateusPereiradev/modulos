from random import choice
sorteio= str(input("Digite aqui o nome dos alunos participantes do sorteio:")).split(",")
print(f"Referente aos participantes do sorteio, o ganhador é {choice(sorteio)}")
'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''