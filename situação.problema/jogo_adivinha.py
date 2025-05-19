# jogo de adivinhação

import random

print("Bem vindo ao jogo de adivinhação!!")
print("")
print("As regras do jogo são:")
print("O computador irá sortiar um número de 1 a 100.")
print("Logo você terá que adivinhar qual é o número.")
print("Obs: quanto mais perto do número sorteado o computador dirá, assim como o quanto mais longe!")
print("")

comp = random.randint(1, 100)

while True:
    n = int(input("Adivinhe o número!: "))
    
    if n > comp:
        print("O número é menor")
        
    elif n < comp:
        print("O número é maior")
        
        
    else:
        print("PARABÉNS!! você acertou o número :) ", comp)
        print("Jogar novamente??")
        print("")
        print("[1] Sim")
        print("[2] Não")
        print("")
        num1 = int(input("Escolha se quer continuar no jogo!: "))
        
        if num1 == 1:
            print("Próxima rodada!")
            comp = random.randint(1, 100)
            
            print("")
        else:
            print("Obrigada por entrar no jogo!!")
            break
        
    