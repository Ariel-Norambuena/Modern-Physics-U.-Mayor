import matplotlib.pyplot as plt
#import plotly.express as px
import numpy as np
import pandas as pd
import time

start_time = time.time()

# Relativistic velocity: Model 1
def getRelativisticVel1(t,m0,q,E,c,w):
   # Electric force
   F = q*E
   # Classic aceleration
   a = F/m0
   # Time function
   ft = (1-np.cos(w*t))/w
   return (a*c*np.abs(ft))/np.sqrt(c**2+(a*ft)**2)

# Relativistic velocity: Model 2
def getRelativisticVel2(t,m0,q,E,c,w):
   # Electric force
   F = q*E
   # Classic aceleration
   a = F/m0
   # Time function
   ft = np.sin(w*t/2)/w
   return (a*c*np.abs(ft))/np.sqrt(c**2+(a*ft)**2)

# Relativistic Kinetic energy
def getRelativisticEnergy(t,m0,q,E,c,w):
   # Relativistic velocity
   v_rel = getRelativisticVel1(t,m0,q,E,c,w)
   # Gamma factor
   gamma = 1/np.sqrt(1-(v_rel/c)**2)
   return m0*c**2*(gamma-1)

# Time-dependent electric field
def getElectricField(t,E,w):
   return E*np.sin(w*t)

##################################
########### MAIN CODE ############

# Import data
data = pd.read_excel (r'DatosExperimentales.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
t_exp = pd.DataFrame(data, columns= ['Tiempo (s)'])
v_exp = pd.DataFrame(data, columns= ['Rapidez (m/s)'])

# Model parameters
w = 2.5133
c = 3e+8;         
q = 1.6e-19;      
E = 25;            
m0 = 1.67e-27;   
F = q*E;        

# Time
t = np.linspace(0,10,10000)   

# Relativistic velocity: Model 1
v_rel1 = getRelativisticVel1(t,m0,q,E,c,w)

# Relativistic velocity: Model 2
v_rel2 = getRelativisticVel2(t,m0,q,E,c,w)

# Relativistic kinetic energy
K_rel = getRelativisticEnergy(t,m0,q,E,c,w)

# Plot velocity vs time
lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(t, v_rel1*1e-8,'-b', linewidth=3, label=r'$Model \; A$'); 
plt.plot(t, v_rel2*1e-8,'-r', linewidth=3, label=r'$Model \; B$'); 
plt.scatter(t_exp, v_exp*1e-8, s= 100,label=r'$Experimental \; data$'); 
plt.xlabel(r'$Tiempo \; (seg)$');plt.ylabel(r'$Velocity \; m/s \times 10^8$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":22})
plt.grid()
plt.xlim(min(t),max(t))
#plt.savefig('Relativistic_vs_Classical_Velocity.png')

# Plot Kinetic energy vs time
lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(t, K_rel,'-b', linewidth=3, label=r'$K_{rel} $'); 
plt.xlabel(r'$Tiempo \; (seg)$');plt.ylabel(r'$Kinetic \; energy \; (J)$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":22})
plt.grid()
plt.xlim(min(t),max(t))

# Velocity and Kinetic Energy at t=12 s
v12 = getRelativisticVel1(12,m0,q,E,c,w)
K12 = getRelativisticEnergy(12,m0,q,E,c,w)

print('Velocidad a los 12 segundos:',v12/c,'c')
print('Energía cinética relativista a los 12 segundos:', K12,'(J)')
    
    
# Relativistic velocity for different values of the electric field amplitude E0
E0 = 1
v1 = getRelativisticVel1(t,m0,q,E0,c,w)
E1 = getElectricField(t,E0,w)
    
E0 = 10
v2 = getRelativisticVel1(t,m0,q,E0,c,w)
E2 = getElectricField(t,E0,w)

E0 = 25
v3 = getRelativisticVel1(t,m0,q,E0,c,w)
E3 = getElectricField(t,E0,w)

lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(v1*1e-8, E1,'-b', linewidth=3, label=r'$E=1 \; V/m$'); 
plt.plot(v2*1e-8, E2,'-r', linewidth=3, label=r'$E=10 \; V/m$'); 
plt.plot(v3*1e-8, E3,'-g', linewidth=3, label=r'$E=25 \; V/m$'); 
plt.xlabel(r'$Velocity \; (m/s)$');plt.ylabel(r'$Electric field \; (V/m)$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":22})
plt.grid()

print("--- %s seconds ---" % (time.time() - start_time))