objetos = ["lápis", "caneta", "estojo", "borracha", "garrafa"]
objetos.append("apontador")
print(objetos[0])

print(objetos.pop(1))

print(len(objetos))
for objeto in objetos: print(objeto)

if "cadeira" in objetos:
    objetos.remove("cadeira")
    
else:
    objetos.append("cadeira")
print(objetos)

print(objetos)
objetos.sort()
print(objetos)


x = len(objetos)
num = objetos[0]
num1 = objetos[x - 1]
print("primeiro", num," e ultimo", num1)

objetos.clear()
      
