
evento = []
presente = []
ausente = []

while True:
    print("")
    print("[0] Cadastro dos participantes ")
    print("[1] Exibir o total de participantes ")
    print("[2] Lista em ordem alfabética ")
    print("[3] Confirmação de presença dos participantes ")
    print("[4] Relatório de paticipantes presentes e ausentes ")
    print("")
    escolha = int(input("Escolha uma das opções: "))
    print("")
   
    if escolha == 1:
        nome = input("Digite o nome: ")
        print("")
        if nome in reuniao:
            print("Este nome já está na lista")
            print("")
        else:
            reuniao.append(nome)
            print("Adicionado")
    elif escolha == 2:
            print(" A lista tem", len(evento ))
    elif escolha == 3:
        evento.sort()
        for nome in evento:
            print(nome)
    elif escolha == 4:
        for nome in evento:
            print(nome)
            consulta = input("Está presente? S/n ")
            print("")
            if  consulta == "Sim":
                presente.append(nome)
                print("Está presente")
            else:
                ausente.append(nome)
                print("Está ausente")
    elif escolha == 5:
        print("Participante presente no evento ")
        for nome in presente:
            print(nome)
            print("")
        print("Participante ausente no evento ")
        for nome in ausente:
            print(nome)
            print("")  
