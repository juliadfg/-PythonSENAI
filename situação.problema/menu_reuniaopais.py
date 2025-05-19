#menu

pais = [""]
pais_ausentes = [""]
pais_presentes = [""]

while True:
    print("")
    print("MENU")
    print("")
    print("[0] - Adicionar nome")
    print("[1] - Exibir número de participantes ")
    print("[2] - Ordem alfabetica")
    print("[3] - Confirmação de presença")
    print("[4] - Relatório da chamada")
    print("")
    escolha = int(input("Escolha um número: "))
    if escolha == 0:
        nome = input("Escreva seu nome ")
        if nome in pais:
            print("Esse nome já está na lista ")
        else:
            pais.append(nome)
            print("Nome adicionado ")
    elif escolha == 1:
        print("A quantidade de pais é ", len(pais))
        
    elif escolha == 2:
        pais.sort()
        print("Lista dos nomes dos pais  ")
        for nome in pais:
            print(nome)
            
    elif escolha == 3:
        for nome in pais:
            print(nome)
            nome_consulta = input("Está presente? (s/n) ")
            if nome_consulta == "s":
                pais_presentes.append(nome)
                print("Pai presente ")
            else:
               pais_ausentes.append(nome)
               print("Pai ausente ")
    
    elif escolha == 4:
        print("Pais presentes ")
        for nome in pais_presentes:
            print("")
            print(nome)
            print("")
        print("Pais ausentes ")
        for nome in pais_ausentes:
            print("")
            print(nome)
            print("")