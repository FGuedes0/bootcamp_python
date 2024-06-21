grau = int(input("Digite a temperatura: "))

if grau <18:
    print("Baixa")
elif 18 <= grau <= 26:
    print("Normal")
else:
    print("Alta")