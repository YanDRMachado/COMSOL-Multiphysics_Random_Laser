'''python 3.7.9'''

'''trapezoidal, sem numpy nem plotlib'''

import math

# f = lambda x: x**2 *math.cos(x) 

# a = 0
# b = math.pi/2
# N = 5 #número de subintervalos
# h = (b-a)/N #"step size"
# S = 1/2 * (f(a) + f(b))

# for i in range(1, n): #no python isso vai de 1 até n-1
#     S += f(a + i*h) #i é o subscrito do nosso x [x1, x2, x3, ...]

# Integral = h*S
# print("Integral = %f" %Integral)


'''implementando numpy, matplotlib e calculando um trapézio singular para aproximar a integral'''

# import numpy as np
# import matplotlib.pyplot as plt

# #plot da função, do trapézio singular que apeoxima a área da integral e cálculo dessa área
# x = np.linspace(-0.5, 1.5, 100)
# y = np.exp(-x**2)
# plt.plot(x,y)

# x0 = 0
# x1 = 1
# y0 = np.exp(-x0**2) 
# y1 = np.exp(-x1**2)
# plt.fill_between([x0,x1],[y0,y1])

# plt.xlim([-0.5, 1.5])
# plt.ylim([0, 1.5])
# plt.show()

# Integral = 0.5*(y1 + y0)*(x1 - x0)
# print("Integral = %f" % Integral)

'''definindo a fórmula trapezoidal como uma função, versão final + erro + plots'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

f = lambda x: np.exp(x**2) #função a ser integrada
a = -1 #início do intervalo de integração
b = 1 #final do intervalo de integração)
N = 1200 #número de subintervalos, ^ número ^ precisão (exceto para funções modulares)
x = np.linspace(a, b, N+1) 
y = f(x)

#função da Fórmula Trapezoidal

def trapezoidalformula(f, a, b, N):
    y_inicial = y[:-1] #início do intervalo
    y_final = y[1:] #final do intervalo
    H = (b-a)/N
    Integral = (H/2) * np.sum(y_inicial + y_final)
    return Integral

#X e Y são os valores para o plot de y=f(x) para a fórmula trapezoidal

X = np.linspace(a, b, 100)
Y = f(X)
plt.figure(figsize = (12, 8))
plt.plot(X,Y)
# plt.plot([0,0],'k--') #reta horizontal correspondente ao eixo x

for i in range(N):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, f(x[i]), f(x[i+1]), 0]
    plt.fill(xs, ys, 'b', edgecolor='r', alpha=0.2)

plt.title('N={}'.format(N))
plt.show()

print("Trapezoidal")
Area = trapezoidalformula(f, a, b, N)
print("Área = ", Area)

#para calcular o erro podemos usar o valor da integral do scipy

Int, E = integrate.quad(f, a, b) #"general purpose integration command"
# print(Int)
print('Erro = ', np.abs(Int - Area))


'''definindo a função para a fórmula Cavalieri-Simpson'''


def cavalierisimpson(f, a, b, N):
    if N % 2 == 1: #caso o resto da divisão N/2 = 1 -> N é impar e deve ser modificado
        raise ValueError('O input N ser par.')
    H = (b-a)/N
    Integral = H/6 * 2 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return Integral

print("Cavalieri-Simpson")
Area = cavalierisimpson(f, a, b, N)
print("Área = ", Area)

Int, E = integrate.quad(f, a, b) #"general purpose integration command"
print('Erro = ', np.abs(Int - Area))


'''função da Fórmula Retangular (Midpoint)'''


def midpoint(f, a, b, N):
    H = float(b-a)/N
    result = 0
    for i in range(N):
        result += f((a + H/2) + i*H)
    result *= H
    return result


print("Midpoint/Rectangular")
Area = midpoint(f, a, b, N)
print("Área = ", Area)

Int, E = integrate.quad(f, a, b) #"general purpose integration command"
print('Erro = ', np.abs(Int - Area))

# plt.title('Fórmula de Cavalieri-Simpson, N={}'.format(N))
# plt.show()
