#capacidade max = 50 litros
#quantidade atual = 20 litros
#adicionar + 30 litros
#valor por litro = 5,80

#1- quantos reais ficou ao encher 30 litros

#2- a quantidade necessária para completar o tanque e o valor em reais

#3- identificar os valores
# subtrair a capacidade max pela quantidade atual
# multiplicar o resultado da subtração pelo preço do combustível
# obter o resultado

num1 = 50
num2 = 20
num3 = 5.80

sub = num1 - num2
mult = sub * num3
print("o custo vai ser de " + str(mult)) 


capacidade = int(input("selecione a capacidade max "))

quant = int(input("selecione a quantidade atual "))

sub = capacidade - quant

result = input("a quantidade disponível é " + str(sub))

valor = float(input("selecione o preço por litro "))

final= sub * valor

print("o preço final é de " + str(final))

