#solicitar os lados do triangulo
#identificar qual o tipo do triangulo

num1 = input( "selecione a medida do lado1 do triangulo ")
num2 = input("selecione a medida do lado2 do triangulo ")
num3 = input("selecione a medida do base do triangulo ")

medida1 = num1 == num2 == num3
medida2 = num1 == num2 != num3
medida3 = num1 != num2 != num3

if medida1:
    print("equilatero")
    
elif medida2:
    print("isosceles")

else:
    print("escaleno")


