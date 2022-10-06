# Fazer um programa que leia dois números por teclado e mostre o seguinte menu:
# Mostrar uma soma dos dois números
# Mostrar um resto dos dois números (o primeiro menos o segundo)
# Mostrar uma multiplicação dos dois números
# Em caso de não introduzir uma opção válida, o programa irá informar que não é correta.

print("Bem-vindo(a)!")
while (True):
    print("""Escolha uma das opções a seguir: 
    1) Somar dois números 
    2) Subtrair dois números
    3) Multiplicar dois números 
    4) SAIR""")

    option = input()
    if option == '1':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("A soma dos dois números é: ", n1 + n2)
    elif option == '2':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("A subtração dos dois números é: ", n1 - n2)
    elif option == '3':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("A multiplicação dos dois números é: ", n1 * n2)
    elif option == '4':
        print("Você escolheu finalizar o programa.")
        break
    else:
        print("Comando desconhecido")
        break