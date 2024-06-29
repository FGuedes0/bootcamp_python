#Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

lista = input("digite uma lista numérica separada por virgulas: ")
lista_dividida = lista.split(",")
pares = []


for lista_dividida in lista_dividida:
    if int(lista_dividida) % 2 == 0:
        pares.append(lista_dividida)

print(pares)