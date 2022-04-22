import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plotly.io as pio
pio.renderers.default='browser'
import time

start_time = time.time()

# Fit function
def objective(x, a, b):
	return a*x + b

# Physical constants
N = 10;               
h = 6.6*1e-34;       
e = 1.6*1e-19;        

# Experimental data
W = e*np.array([2.28, 4.08, 6.35])
f = np.linspace(10e+12,120e+13,10)

V = np.array([[-2.3387,   -4.1387,   -6.4087],
   [-1.5933,   -3.4233,   -5.6633],
   [-1.1879,   -3.0479,   -5.2179],
   [-0.6525,   -2.3025,   -4.1725],
   [-0.0521,   -2.1571,   -4.1271],
   [0.4783,   -1.2117,   -3.4817],
   [1.1338,   -0.8662,   -3.3362],
   [1.5192,   -0.4508,   -2.5908],
   [1.9646,    0.3346,   -1.9554],
   [2.6200,    0.9700,   -1.4500]])

# Plot data
lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.scatter(f*1e-13,V[:,0], s= 200,label=r'$Na$'); 
plt.scatter(f*1e-13,V[:,1], s= 200,label=r'$Al$'); 
plt.scatter(f*1e-13,V[:,2], s= 200,label=r'$Pt$'); 
plt.xlabel('Frequency (Hz x 10^13) ');plt.ylabel('Stopping potential (V)')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":20})
plt.grid()

## Fitting Einstein model for Sodium, Aluminium and Platinum
data = np.array([0,1,2])

# Fit frequency 
f_fit = np.linspace(10e+12,120e+13,100)

# Fit function
Vfit = np.zeros([100,3])

# Parameters for each element
Param = np.zeros([2,3])

# Plot data
lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
for n in data:
    popt, _ = curve_fit(objective, f, V[:,n])
    a, b = popt
    # calculate the output for the range
    Vfit[:,n] = objective(f_fit, a, b)
    Param[0,n] = a
    Param[1,n] = b
    

# Plot data
lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.scatter(f*1e-13,V[:,0], s= 200,label=r'$Na$'); 
plt.scatter(f*1e-13,V[:,1], s= 200,label=r'$Al$'); 
plt.scatter(f*1e-13,V[:,2], s= 200,label=r'$Pt$'); 
plt.plot(f_fit*1e-13, Vfit[:,0] ,'-r', linewidth=3); 
plt.plot(f_fit*1e-13, Vfit[:,1] ,'-b', linewidth=3); 
plt.plot(f_fit*1e-13, Vfit[:,2] ,'-g', linewidth=3); 
plt.xlabel('Frequency (Hz x 10^13) ');plt.ylabel('Stopping potential (V)')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop={"size":20})
plt.grid()
plt.ylim(-8,4)

# Experimental values for Sodium (n=0)
n = 0
h = Param[0,n]*e*1e34;
W = -Param[1,n];
print('Planck constant Na = %.5f (10^34)\nWork function Na = %.5f (eV) \n' % (h, W))

# Experimental values for Aluminium (n=1)
n = 1
h = Param[0,n]*e*1e34;
W = -Param[1,n];
print('Planck constant Al = %.5f (10^34) \nWork function Al = %.5f (eV) \n' % (h, W))

# Experimental values for Sodium (n=2)
n = 2
h = Param[0,n]*e*1e34;
W = -Param[1,n];
print('Planck constant Pt = %.5f (10^34) \nWork function Pt = %.5f (eV) \n' % (h, W))

# Average Planck Constant
h = np.average(Param[0,:])*e*1e34
print('Average Planck constant = %.5f x10^34 \n \n' % h)



print("--- %s seconds ---" % (time.time() - start_time))