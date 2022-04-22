import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default='browser'
import numpy as np
import time

start_time = time.time()

# Physical parameters
me = 9.1e-31       
c = 3e+8
h = 6.62607015e-34
E = me*c**2

# Angle
theta = np.linspace(0,2*np.pi,10000) 

# Energies for the incoming photon
Egamma = np.array([0.01*E, 0.1*E, E, 10*E])


lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
# Plotting
Leg = ["\u03B1 = 0.01","\u03B1 = 0.1","\u03B1 = 1","\u03B1 = 10"]
n = 0
for Eg in Egamma:
    alpha = Eg/E
    Egammap = Eg/(1+alpha*(1-np.cos(theta)))
    plt.plot(theta*180/(np.pi), Egammap/Eg, linewidth=3, label=Leg[n]); 
    n+= 1;
    
plt.xlabel(r'$\theta \; (°)$')
plt.ylabel(r'$E_{\gamma^{\prime}}/E_{\gamma} $')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":18})
plt.ylim((0, 1.2))
plt.xticks(range(0,420,60))
plt.grid()
plt.savefig('EfectoCompton.png')


# Energy conservation
Egamma = 2*E
alpha = Egamma/E
Egammap = Egamma/(1+alpha*(1-np.cos(theta)))
Eelectron = E+Egamma-Egammap

lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(theta*180/(np.pi), Egammap, '-b', linewidth=3, label=r'$E_{\gamma^{\prime}}$'); 
plt.plot(theta*180/(np.pi), Eelectron,'-r',  linewidth=3, label=r'$E_{e}$'); 
plt.xlabel(r'$\theta \; (°)$')
plt.ylabel(r'$Energy$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":20})
plt.xticks(range(0,420,60))
plt.grid()



print("--- %s seconds ---" % (time.time() - start_time))