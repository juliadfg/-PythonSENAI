#solicite 2 notas
#calcule a media
#se for >= 70 exibir aprovado
#se for <= 50 exibir reprovado

num1 = int(input("selecione a primeira nota "))
num2 = int(input("selecione a outra nota "))

media = num1 + num2
resu_media = media / 2

if resu_media >= 70 and resu_media == 100:
    print("Aprovado ")
    
elif resu_media >= 50 or resu_media == 70:
    print("Recuperação ")
    
else:
    print("Reprovado ")
    
    