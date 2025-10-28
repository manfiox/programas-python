import os 
import math
import random


#funções para raiz quadrada
def raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print ("Não é posível calcular a raiz quadrada de um número negativo.")
    else: 
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
    input("Pressine qualquer tecla para continuar...")


#funções para calcular potencia
def calcular_potencia():
    base = float(input("Digite a base:"))
    expoente = float(input("Digite o expoente:"))
    resultado = math.pow (base, expoente)
    print (f"O resultado de {base} elevado a {expoente} é igual a {resultado}")
    input ("Pressine qualquer tecla para continuar...")


#função para gerar número randomico
def numero_aleatorio():
   inicio = int(input("Digite o valor inicial do intervalo: "))
   fim = int(input("Digite o valor final do intervalo: "))
   if inicio > fim:
       print("Intervalo inválido! O valor inicial deve ser menor ou igual ao valor final.")
   else:
       resultado = random.randint(inicio, fim)
       print(f"Número aleatório gerado entre {inicio} e {fim}: {resultado}")


#função para calcular operações básicas
def calculos_basicos():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    print(f"\n=== Resultados das operações entre {numero1} e {numero2} ===")
    
    # Adição
    adicao = numero1 + numero2
    print(f"Adição: {numero1} + {numero2} = {adicao}")
    
    # Subtração
    subtracao = numero1 - numero2
    print(f"Subtração: {numero1} - {numero2} = {subtracao}")
    
    # Multiplicação
    multiplicacao = numero1 * numero2
    print(f"Multiplicação: {numero1} × {numero2} = {multiplicacao}")
    
    # Divisão
    if numero2 != 0:
        divisao = numero1 / numero2
        print(f"Divisão: {numero1} ÷ {numero2} = {divisao}")
    else:
        print("Divisão: Não é possível dividir por zero!")
    
    # Potência
    potencia = numero1 ** numero2
    print(f"Potência: {numero1} elevado a {numero2} = {potencia}")
    
    input("\nPressione qualquer tecla para continuar...")

        
#Menu principal com as operações
def main():
    while True:
        os.system("cls")
        print("\n=== Menu de Operações ===")
        print("1. Calcular Raiz Quadrada")
        print("2. Calcular Potência")
        print("3. Gerar Número Aleatório")
        print("4. Cálculos Básicos")
        print("5. Sair")
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            raiz_quadrada()
        elif escolha == '2':
            calcular_potencia()
        elif escolha == '3':
            numero_aleatorio()
        elif escolha == '4':
            calculos_basicos()
        elif escolha == '5':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressine qualquer tecla para continuar...")

if __name__ == "__main__":
    main()
