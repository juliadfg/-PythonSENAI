quant = 0
valor_total = 0

while True:
    print("Escolha uma opção ")
    print("menu ")
    print("[0] - Sair ")
    print("[1] - Mostrar a quantidade e o valor total das despesas ")
    print("[2] - Adicionar o valor da despesa ")
    escolha = int(input("Escolha um número "))
    if escolha == 0:
        break
    
    elif escolha == 1:
        print("A quantidade é ", quant, "e o valor total é ", valor_total )
    elif escolha == 2:
        valor = int(input("Digite um valor de despesa "))
        quant = quant + 1
        valor_total = valor_total + valor

