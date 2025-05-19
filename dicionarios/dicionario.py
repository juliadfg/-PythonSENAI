#tema filme

filme1 = {
    "nome": "BEE MOVIE",
    "genero": "comédia" ,
    "tempo": 1.3,
    "assistido": True
}

filme2 = {
    "nome": "Coraline e o Mundo Secreto",
    "genero": "terror" ,
    "tempo": 1.4,
    "assistido": True
}

filme3 = {
    "nome": "Carros",
    "genero": "ação" ,
    "tempo": 1.5,
    "assistido": False 
}

# Exibir uma lista de Dicionários
lista_filme = [filme1, filme2, filme3]


    # Escolhendo os campos
for filme in lista_filme:
    print(f"{filme['genero']}")
    
    # Exibindo todos
for filme in lista_filme:
    for chave, valor in filme.items():
        print(f"{chave} - {valor}")
    print()
    









