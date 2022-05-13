import numpy as np
from matplotlib import pyplot as plt
import time

start_time = time.time()

# Geometrical parameters
# Physical parameters
a = 3
d = 6*a
wavelength = 5*0.65
L = 10*d
xmin, xmax = 0, 100*d
ymin, ymax = -20*d, 20*d
# Number of points for the grid
Npoints = 1500
xpoints, ypoints = Npoints, Npoints

# Array for x and y coordinates
x = np.linspace(xmin, xmax, xpoints)
y = np.linspace(ymin, ymax, ypoints)

# 2D meshgrid
X, Y = np.meshgrid(x,y)

# Points
points = np.concatenate([X.reshape(-1, 1), Y.reshape(-1, 1)], axis=-1)

# Source point: single slit as different individual source points
# Amplitude and wavevector
A1 = 1
k = 2*np.pi/wavelength
wave = 0
Nsources = 100
sep = np.linspace(-a/2,a/2,Nsources)

for n in range(0,Nsources):
    source = np.array([0,sep[n]])
    points1 = points - source
    # Waves
    xx1 = (points1[:,0]**2+points1[:,1]**2)**0.5
    wave = wave + A1*np.sin(k*xx1)


# PLot of the interference pattern
Intensity = wave**2
plt.figure(figsize=(7, 7))
plt.xlim(xmin, xmax)
plt.ylim(-10*d, 10*d)
plt.scatter(points[:, 0], points[:, 1], c = Intensity, cmap=plt.cm.binary)
for n in range(0,Nsources):
    source1 = np.array([0,sep[n]])
    plt.scatter(*source1, c='red')




# Intensity on the screen

d1 = np.zeros(Npoints)
wave1_screen, theta = np.zeros(Npoints), np.zeros(Npoints)
for n in range(0,Npoints):
    yn = y[n]
    r = np.array([xmax, yn])
    theta[n] = 360*np.arctan(yn/xmax)/(2*np.pi)
    for m in range(0,Nsources):
        source1 = np.array([0,sep[m]])
        d1 = np.linalg.norm(r-source1)
        wave1_screen[n] = wave1_screen[n] + A1*np.sin(k*d1)



# Total wave
A = wave1_screen 
Intensity_screen = A**2

lineW = 2 # Line thickness
plt.figure(figsize=(10,6), tight_layout=True)
plt.plot(theta,Intensity_screen,'-r', linewidth=2); 
plt.ylabel(r'$Intensity$');plt.xlabel(r'$\theta\; (degrees)$')
axes = plt.gca()
axes.xaxis.label.set_size(22)
axes.yaxis.label.set_size(22)
plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)


print("--- %s seconds ---" % (time.time() - start_time))