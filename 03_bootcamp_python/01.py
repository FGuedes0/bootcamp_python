#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
try:
    quantidade = int(input("Digite a Quantidade: "))
    preco = int(input("Digite o Preço: "))

    if (quantidade or preco) < 0:
        print("Dados inválidos")
    else:
        print("Dados Válidos")
except ValueError:
    print("O valor inserido precisa ser um número")