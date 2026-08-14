# Executa uma operação simples com 2 números inputáveis
num1 = int(input("Coloque o 1º número: "))
num2 = int(input("Coloque o 2º número: "))

opcao = input("Escolha entre as seguintes opções...s\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Potenciação\n6. Radiciação\nDigite seu número: ")

def executar_op(numero1, numero2, operacao):
    if operacao == "1":
        print(numero1 + numero2)
    elif operacao == "2":
        print(numero1 - numero2)
    elif operacao == "3":
        print(numero1 * numero2)
    elif operacao == "4":
        print(numero1 / numero2)
    elif operacao == "5":
        print(numero1**numero2)
    else:
        print(numero1**(1/numero2))

executar_op(num1, num2, opcao)
