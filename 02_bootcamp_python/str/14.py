#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Digite uma data no formado 'dd/mm/aaaa': "))
data = data.split("/")
print(data[0])
print(data[1])
print(data[2])