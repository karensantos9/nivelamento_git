import matplotlib.pyplot as plt
import numpy as np

def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 14
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    print(" " + "_" * maximoCaracteresPorLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maximoCaracteresPorLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " +
              linha.center(maximoCaracteresPorLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " *
              maximoCaracteresPorLinha + padding * " " + "|")
    print("|" + "_" * maximoCaracteresPorLinha + 2 * padding * "_" + "|")
    

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


def plot_linear(x,a,b):
        axisX = np.linspace(-10, 10 ,100)
        axisY= linear( axisX ,a,b)
        plt.plot(axisX, axisY, marker= 'o')
        plt.title(f'grafico da função linear')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    

def exponencial(a, x):
    resultado = a ** x
    return resultado
 

def plot_exponencial(valor1, valor2):
    x = np.linspace(-6, 6, 10)
    y = exponencial (valor1, x)
    plt.plot(x,y)
    plt.title(f'gráfico da função exponencial {valor1}**{valor2}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def funcao_quadratica(x, a, b, c):
    resultado = a * x ** 2 + b * x *c
    return resultado

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        raiz_delta = delta ** 0.5
        raiz1 = (-b + raiz_delta) / (2*a)
        raiz2 = (-b - raiz_delta) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return ('erro')

def plot_quadratica(a, b, c):
    x_values = np.linspace(-10, 10,10)
    y_values = funcao_quadratica(x_values, a, b, c)
    plt.plot(x_values,y_values)
    plt.title(f'gráfico da função quadratica ')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def fatorial(n):
    if n < 0:
            return "erro"
    elif n == 0:
            return 1
    else:
            resultado = 1
            for i in range (1, n + 1):
                resultado *= i
            return resultado     

def plot_fatorial(n):
        x = list(range(n+1))
        y = [fatorial(i) for i in x]
        plt.plot(x,y, marker='x', linestyle='-')
        plt.title('gráfico de fatorial')
        plt.xlabel('número')
        plt.ylabel('fatorial')
        plt.grid('true')
        plt.show()


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
                    x = int(input("digite o primeiro valor: "))
                    y = int(input("digite o segundo valor: "))
                    resultadosoma = soma (x,y)
                    print (resultadosoma)
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    x = int(input("digite o primeiro valor: "))
                    y = int(input("digite o segundo valor: "))
                    resultadosub = soma (x,y)
                    print (resultadosub)
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    x = int(input("digite o primeiro valor: "))
                    y = int(input("digite o segundo valor: "))
                    resultadomult = soma (x,y)
                    print (resultadomult)
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    x = int(input("digite o primeiro valor: "))
                    y = int(input("digite o segundo valor: "))
                    resultadodivi = soma (x,y)
                    print (resultadodivi)
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    a = int(input("digite o valor de a: "))
                    x = int(input("digite o valor do expoente: "))
                    resultadoexpo = exponencial(a,x)
                    print(resultadoexpo)
                    grafico = plot_exponencial(a,x)
                    print(grafico)
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    a = int(input("digite o valor de a: "))
                    b = int(input("digite o valor de b: "))
                    c = int(input("digite o valor do c: "))
                    print(
                        f"o resultado das raízes ou da raíz é/são: {calcular_raizes(a,b,c)}")
                    plot_quadratica(a,b,c)
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    a = int(input("digite o valor de a: "))
                    b = int(input("digite o valor de b: "))
                    x = int(input("digite o valor de x: "))
                    
                    print(
                        f"o resultado é:{linear(a,b,x)}")
                    plot_linear(x,a,b)
                    
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL n!")
                    n = int(input("escolha o valor: "))
                    print (f" o resultado do fatorial é: {fatorial(n)}")
                    plot_fatorial(n)
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()