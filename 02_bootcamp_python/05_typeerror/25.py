#Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista = input("Insira uma lista de números separada por vírgulas: ")

try:
    lista.replace(" ","")
    lista = lista.split(",")
    for i in range(0, len(lista)):
        lista[i] = int(lista[i].strip())    
    print(lista)
except:
    print("A lista deve conter apenas números")