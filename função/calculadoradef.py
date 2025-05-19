#menu 
 
 
def calcular_despesas():
    float(input("Adicione o valor da despesa "))
    
calcular_despesas()

[0]sair
[1]adicionar valor de despesa
[2]mostrar a quantidade e o valor total das despesas 

def adiçao (num1, num2):
    return num1 + num2

def calculo(contas):
    print("Soma", adicao(num1, num2))
    print("Subtração", sub(num1, num2))
    print("Multiplicação", mult(num1, num2))
    print("Divisão", div(num1, num2))
opcao = int(input("Escolha uma opção(1,2,3,4)"))
   
num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
   
if opcao == 1:
    print("Soma", adiçao(num1, num2))
elif opcao == 2:
    print("Subtração", sub(num1, num2))
elif opcao == 3:
    print("Multiplicação", mult(num1, num2))
else:
    print("Divisão", div(num1, num2))
   