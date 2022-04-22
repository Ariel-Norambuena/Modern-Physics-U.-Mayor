import math
import matplotlib.pyplot as plt 
import numpy as np

h = 1
g = 9.8
# Aceleracion
Ai = 0
Af = 0.999*g  # Mostrar que pasa si acercamos Af al valor 0.999999*g
N = 100000
dA =(Af-Ai)/(N)
A = np.arange(Ai,Af,dA)

# Tiempo de vuelo
t_vuelo = np.zeros([1,N])

for n in range(1,N+1):
    t_vuelo[0][n-1] = math.sqrt(2*h/(g-A[n-1]))
    
T_vuelo = t_vuelo[0][:]    
# Plot

lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(A/g, T_vuelo ,'-r', linewidth=3,label=r'$t_{vuelo}$'); 
plt.ylabel(r'$Tiempo \; de \; vuelo \; (seg)$');plt.xlabel(r'$A/g$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":20})
plt.grid()
plt.savefig('Tiempo_Vuelo.png')

