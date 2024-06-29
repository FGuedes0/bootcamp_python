#Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = str(input("Digite um texto, se possível com palavras repetidas: "))
palavras = texto.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] +=1
    else:
        contagem[palavra] = 1
print(contagem)