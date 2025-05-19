# calcular a area do hexagono com o numero solicitado

# caulcular a area do triangulo para achar a area do hexagono

# passo1 = obter a formula
# passo2 = solicitar a escolha de um numero
# passo3 = elevar o numero escolhido ao quadrado
# passo4 = resolver a raiz de 3 da formula
# passo5 = multiplicar o numero ao quadrado com a raiz de 3
# passo6 = dividir esse resultado por 4
# passo7 = multiplicar o resultado da area do triangulo por 6
# passo8 = exibir o resultado da area do hexagono

num1 = int(input("Digite um numero "))

mult1 = num1 * num1
raiz = round(3**0.5, 2) * mult1
div = raiz / 4
areah = div * 6

print("A area do hexagono é " + str(areah))