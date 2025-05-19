# solicite um numero ao usuario
# exiba todos os numeros pares
# quantidade deles ate o numero solicitado

num1 = int(input("solicite um número inteiro "))
quant = 0 
n = 0

while n <= num1:
    if n % 2 == 0:
       print(n)
       quant = quant + 1
    n = n + 1
    
print("A quantidade de números pares é" , quant)
