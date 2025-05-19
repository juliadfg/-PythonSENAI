#jogo par ou ímpar

import random

print("Bem vindo ao jogo de Par ou Ímpar!:)")
print("")
print("As regras do jogo são: Escolha entre Par ou Ímpar, depois digite um número de 1 a 10")
print("Depois com a soma dos números veremos se será par ou ímpar!")
print("")

impar = 1, 3, 5, 7, 9
par = 2, 4, 6, 8, 10


while True:
    print("Par ou Ímpar?? ")
    print("")
    print("[1] Par")
    print("[2] Ímpar")
    print("[3] Sair")
    print("")
    num = int(input("Escolha um número do menu: "))
    
    
    if num == 1:
        print("Escolha um número de 1 a 10 ")
   
    elif num == 2:
        print("Escolha um número de 1 a 10 ")
        
    else:
        print("Obrigado por abrir o jogo! até a próxima <3")
        break
        

    num1 = int(input("Digite seu número: "))
    num2 = random.randint(1, 10)

    print("Seu número:", num1)
    print("Meu número:", num2)

    soma = num1 + num2

    if soma % 2 == 0:
        if num == 1:
            print("Você ganhou!")
        else:
            print("Você perdeu!")
            
    else:
       
        
        if num == 2:
            print("Você ganhou!")
        else:
            print("Você perdeu!")
            
    
    