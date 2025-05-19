def calculo_fahrenheit(celsius):
    return celsius * 1,8 + 32

def calculo_kelvin(celsius):
    return celsius + 273

temp = float(input("Digite a temperatura em Celsius "))

print("A temperatura em fahrenheint", calculo_fahrenheit(temp))
print("A temperatura do Kelvin", calculo_kelvin(temp))