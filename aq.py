import matplotlib.pyplot as plt
while True:
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
        
    exemplo = int(input("insira: "))
    print(plot_fatorial(exemplo))