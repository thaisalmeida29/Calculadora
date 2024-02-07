print("****************CALCULADORA EM PYTHON*******************")

print("Selecione o número da opção desejada: \n"
          "1 - Soma \n" 
          "2 - Subtração \n"
          "3 - Multiplicação \n"
          "4 - Divisão \n")

operacao = input("Digite sua opção (1/2/3/4): ")
if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida. Tente novamente. \n")
     # Reinicia o loop

valor_1 = int(input("Digite o primeiro número: "))
valor_2 = int(input("Digite o segundo número: "))

def Calcular():
     if operacao == "1":
            soma = valor_1 + valor_2
            print(valor_1, "+", valor_2, "=", soma, "\n")
     elif operacao == "2":
            subtracao = valor_1 - valor_2
            print(valor_1, "-", valor_2, "=", subtracao, "\n")
     elif operacao == "3":
            multiplicacao = valor_1 * valor_2
            print(valor_1, "*", valor_2, "=", multiplicacao, "\n")
     elif operacao == "4":
         if valor_2 != 0:
               divisao = valor_1 / valor_2
               print(valor_1, "/", valor_2, "=", divisao, "\n")
         else:
            print("Não é possível dividir por zero. Tente novamente.")
Calcular()

