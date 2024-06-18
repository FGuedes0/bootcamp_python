#receber o nome e printar quantidade de caracteres
try:
    nome = input("Digite seu nome: ")
    if len(nome) == 0:
        raise ValueError("O nome não pode estar em branco")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números")
    elif len(nome.strip()) == 0:
        raise ValueError("Você digitou apenas espaços")
    else:
        tamanho = len(nome)               
        print(tamanho)
        print(nome)
except ValueError as e:
    print(e)