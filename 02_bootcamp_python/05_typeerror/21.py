#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    n1 = float(input("Digite uma temperatura em °C para ser convertida em Fahrenheit: "))
    convertido = (n1 * 9/5)+32
    print(convertido)
except ValueError:
    print("O valor inserido não é válido")


