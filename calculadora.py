while True:
    print()
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    op = input('Digite um operador: ')
    sair = input('Deseja sair? s/n ').lower().strip()

    if sair == 's':
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número!')
        continue  # se o usuário n digitar um número, o while reseta

    n1 = int(n1)
    n2 = int(n2)

    # +,-,*,/

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    else:
        print('Operador inválido!')