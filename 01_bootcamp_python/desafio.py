#digite nome
#digite salário
#digite % do bonus
#calcular valor bonus - 1000 + salário + bonus

cont_bonus = 1000

try:
    nome = input("Digite seu nome: ")
    if len(nome) == 0:
        raise ValueError("O nome não pode estar em branco")
    
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números")
    
    elif len(nome.strip()) == 0:
        raise ValueError("Você digitou apenas espaços")
    
    else:
        try:
            salario = float(input("Digite o salário: "))

        except ValueError:
            print("O valor digitado deve ser um número")

        else:
            try:   
                bonus = float(input("Digite a porcentagem do bonus: "))

            except ValueError:
                print("O valor digitado deve ser um número")

            else:
                valor_bonus = cont_bonus + salario + ((salario * bonus)/100)

                print(f"O salário do usuário {nome} é de: {salario}, O  valor do bonus do usuário {nome} é igual a: {valor_bonus}")

except ValueError as e:
    print(e)

except KeyboardInterrupt:
    print("Parece que você não quer digitar um valor")
        
#fiz antes de ver o exemplo rs
#print("O salário do usuário", nome, "é de:",salario,", o  valor do bonus do usuário", nome, "é igual a:", valor_bonus)