const_bonus = 1000

nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar em branco")
        
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números")
        
        elif len(nome.strip()) == 0:
            raise ValueError("Você digitou apenas espaços")

        else:
            print(f"Nome válido: {nome}")
            nome_valido = True

    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("Parece que você não quer digitar um valor")
        

while not salario_valido:
    try:
        salario = float(input("Digite o salário: "))
        while salario <= 0:
            try:
                salario = float(input("O salário deve ser maior do que 0: "))
            except ValueError:
                print("O valor digitado deve ser um número")
            
    except TypeError:
        print("O valor digitado deve ser um número")
    except KeyboardInterrupt:
        print("Parece que você não quer digitar um valor")
    except ValueError as e:
        print(e)

    else:
        print(f"Salário Válido: {salario}")
        salario_valido = True
    
while not bonus_valido:
    try:   
        bonus = float(input("Digite a porcentagem do bonus: "))

    except TypeError:
        print("O valor digitado deve ser um número")
    except KeyboardInterrupt:
        print("Parece que você não quer digitar um valor")
    except ValueError as e:
        print(e)

    else:
        bonus_valido = True
        print(f"valor do bonus válido: {bonus}")
        valor_bonus = const_bonus + salario + ((salario * bonus)/100)

        print(f"O salário do usuário {nome} é de: R${salario:.2f}, O  valor do bonus do usuário {nome} é igual a: R${valor_bonus:.2f}")