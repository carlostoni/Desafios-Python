#1. Interpretador de Expressões Matemáticas
#Crie um interpretador que analise e resolva expressões matemáticas arbitrárias com suporte a operadores 
#como +, -, *, /, ^ (potência) e parênteses. Sem usar eval() ou ast.literal_eval()!

def calculadora():

    print('''Digite o numero da opercao desejada
          1 - Adicao
          2 - Subtracao
          3 - Multiplicacao
          4 - Divisao
          5 - Potência 
          6 - Parênteses''')
calculadora()
escolha = int(input())

if escolha == 1:
    n = int(input("Digite primeiro número "))
    n2 = int(input("Digite segundo número "))
    print(n + n2)

elif escolha == 2:  
    n = int(input("Digite primeiro número "))
    n2 = int(input("Digite segundo número "))
    print(n - n2)

elif escolha == 3:  
    n = int(input("Digite primeiro número "))
    n2 = int(input("Digite segundo número "))
    print(n * n2)

elif escolha == 4:  
    n = int(input("Digite primeiro número "))
    n2 = int(input("Digite segundo número "))
    print(n / n2)

elif escolha == 5:  
    n = int(input("Digite primeiro número "))
    n2 = int(input("Digite segundo número "))
    print(n ** n2 )
else:
    n = int(input("Digite primeiro número 6 "))
