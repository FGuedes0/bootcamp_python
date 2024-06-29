#Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


try:
    grau = int(input("Digite a temperatura: "))

    if grau < 18:
        print("Baixa")
    elif 18 <= grau <= 26:
        print("Normal")
    else:
        print("Alta")
except ValueError:
    print("Dados inválidos")