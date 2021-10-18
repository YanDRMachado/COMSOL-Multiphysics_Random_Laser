'''python 3.7.9'''

# x = [0, 20, 40, 60, 80, 105]
# y = [26.0, 48.6, 61.6, 71.2, 74.8, 78.2]

# m = len(x)
# n = m - 1 #grau do polinômio de interpolação

# xp = float(input('Input x: '))
# yp = 0

# for i in range(n+1):
#     p = 1
#     for j in range(n+1):
#         if j != i:
#             p *= (xp - x[j])/(x[i] - x[j])
#         yp += y[i]*p

# print('Para x = %.2f, y = %f' %(xp, yp))


'''implementando numpy, arrays'''

# import numpy as np

# x = np.array([0, 20, 40, 60, 80, 100], float)
# y = np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float)

# # m = len(x)
# # n = m - 1 #grau do polinomio

# xp = float(input('Input x: '))
# yp = 0

# for xi,yi in zip(x,y): #os valores serão tomados do array x para cada x[i]
#     p = np.prod((xp - x[x != xi]) / (xi - x[x != xi])) #aplicando as condições dentro do valor 
#     yp += yi * p
        
# print('Para x = %.2f, y = %f' %(xp, yp))


'''optimizado, plotlib + gráfico'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 15, 25, 35, 50, 75, 90, 105, 120], float)
y = np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2, 88.3, 95.4, 109.0], float)

xplt = np.linspace(x[0],x[-1], 1000) #x0 e x-1 são o primeiro e último valores do array, [N pontos do plot]
yplt = np.array([], float) #deixar em branco pois conforme ele roda a gente vai enviando os valores do y

for xp in xplt: #agora o xp terá os valores dos N pontos dentro do xplt
    yp = 0

    for xi,yi in zip(x,y): #os valores serão tomados do array x para cada x[i]
        yp += yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi])) #aplicando as condições dentro do valor
    yplt = np.append(yplt,yp) #np.append não altera o yplt sem o assignment (=) pro LHS
    
#plot
plt.plot(x,y,'ro',xplt,yplt,'b') #plot dos pontos, r=red, o=circles, b=blue, -=continuous line
plt.xlabel('x')
plt.ylabel('y')
print(xplt)
print(yplt)
