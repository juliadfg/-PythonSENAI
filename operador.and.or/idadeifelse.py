#solicite o ano de nascimento
#calcule a idade
#verificar a faixa hetaria

num1 = int(input("selecione o ano de nascimento "))
num2 = int(input("selecione o ano atual "))

idade = num2 - num1

if idade <= 10 or idade == 10:
    print("criança")
    
elif idade <= 11 and idade == 17:
    print("Adolescente")

elif idade <= 18 and idade == 59:
    print("Adulto")
    
else:
    print("idoso")