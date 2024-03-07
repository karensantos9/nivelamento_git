import matplotlib.pyplot as plt
import numpy as np

while True:
    def linear(x,a,b):
        return a*x+b
        
    def plot_linear(a,b):
        axisX = np.linspace(-10, 10 ,100)
        axisY= linear(axisX,a ,b)
        plt.plot(axisX, axisY, marker= 'o')
        plt.title(f'grafico da função linear{a}x + {b}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    break
print (plot_linear(3,4))