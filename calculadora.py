print("===============================")
print("   CALCULADORA PYTHON   ")
print("===============================")
print("1. Adição")
print("2. Subtraçaõ")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")
opcao = input("Escolha uma opção: ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if opcao == "1":
    resultado = numero1 + numero2
    print("resultado: ", resultado)
elif opcao == "2":
    resultado = numero1 - numero2
    print("resultado: ", resultado)
elif opcao == "3":
    resultado = numero1 * numero2
    print("resultado: ", resultado)
elif opcao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("resultado: ", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
elif opcao == "5":
    print("programa encerrado.")
    print("obrigado por ultilizar a calculadora.")

    
