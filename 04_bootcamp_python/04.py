# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
contagem: dict = {}

def contador_de_letras(caracteres):
    for caractere in caracteres:
        contagem[caractere] = contagem.get(caractere, 0) + 1
        #print(contagem)
    return contagem

caracteres: str = str(input("Digite uma frase: "))

contador_de_letras(caracteres)

print(contagem)
