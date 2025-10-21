import os

while True:
    os.system("cls")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # calcula a multiplicação
    resultado = num1 * num2

    # exibe o resultado
    print(f"\nA multiplicação de {num1} x {num2} é {resultado}")

    # pergunta se o usuário quer continuar
    
    continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
   
    #se a resposta for 'n', encerra o programa
    if continuar != 's':
        print("\nFim do programa, até logo!")
        break

print("-" * 40) #separador visual



