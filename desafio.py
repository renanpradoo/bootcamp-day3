CTE = 1000

while True:
    try:
        name = input('Digite seu nome: ')
        if(len(name)) == 0:
            raise ValueError('Nome nao pode estar vazio')
            # exit()
        elif any(char.isdigit() for char in name):
            raise ValueError('Nao pode conter numeros no nome.')
            # exit()
        else:
            break
    except ValueError as e:
        print(e)
        # exit()

while True:
    try:
        salario = float(input('Digite seu salario: '))
        if salario < 0:
            raise ValueError('Salario nao pode ser negativo.')
            # exit()
        else:
            break
    except ValueError as e:
        print(e)    

while True:
    try:
        bonus = float(input('Digite seu bonus: '))
        if bonus < 0:
            raise ValueError('Bonus nao pode ser negativo.')
            # exit()
        else:
            break
    except ValueError as e:
        print(e)    

bonus_final = CTE + salario * bonus
print(f'{name}, seu bonus final eh: {bonus_final:.0f}')
