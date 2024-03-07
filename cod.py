import matplotlib.pyplot as plt
import numpy as np

calculator = """
 _______
|  _____  |
| |_____| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____| |
|_______|
    """
print(calculator)


def soma(x, y):
    
    operacaosoma = x + y
    return operacaosoma

def subtracao(x, y):
   
    operacaosubt = x - y
    return operacaosubt


def multiplicacao(x, y):

    operacaomult = x * y
    return operacaomult


def divisao(x, y):
 
    operacaodiv = x / y
    return operacaodiv 


def linear(x, a, b):
 
    resultado = (a * x)+ b
    return resultado


def plot_linear(resultado):
    plt.plot(linear(resultado))

def exponencial(a, x):
 

def plot_exponencial(x, y):
    


def funcao_quadratica(x, a, b, c):



def calcular_raizes(a, b, c):



def plot_quadratica(a, b, c):



def fatorial(n):

    

def plot_fatorial(n):


def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    print("Faça o código")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    print("Faça o código")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    print("Faça o código")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    print("Faça o código")
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    print("Faça o código")
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    print("Faça o código")
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    print("Faça o código")
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL f(x) = (a * x + b)")
                    print("Faça o código")
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()