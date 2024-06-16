#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

palavra = input("Digite uma palavra que é um palindromo: ")
print(type(palavra))
if isinstance(palavra, str):
    formatado = palavra.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

else:
    print("ERRO: O valor inserido deve ser uma palavra ou frase")