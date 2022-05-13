import numpy as np
from matplotlib import pyplot as plt
import time

start_time = time.time()

# Physical parameters
a = 3
d = 6*a
wavelength = 0.65
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

# Source points
source1 = np.array([0,d/2])
source2 = np.array([0,-d/2])

points1 = points - source1
points2 = points - source2

# Amplitude and wavevector
A1 = 10
A2 = 10
k = 2*np.pi/wavelength

# Waves
Nsources = 100
sep1 = np.linspace(d/2-a/2,d/2+a/2,Nsources)
sep2 = np.linspace(-d/2-a/2,-d/2+a/2,Nsources)

wave1, wave2 = 0, 0

for n in range(0,Nsources):
    # Wave1 
    source1 = np.array([0,sep1[n]])
    points1 = points - source1
    xx1 = (points1[:,0]**2+points1[:,1]**2)**0.5
    wave1 = wave1 + A1*np.sin(k*xx1)
    
    # Wave 2
    source2 = np.array([0,sep2[n]])
    points2 = points - source2
    xx2 = (points2[:,0]**2+points2[:,1]**2)**0.5
    wave2 = wave2 + A1*np.sin(k*xx2)

# Total wave
A = wave1 + wave2
Intensity = A**2

# PLot of the interference pattern
plt.figure(figsize=(7, 7))
plt.xlim(xmin, xmax)
plt.ylim(-10*d, 10*d)
plt.scatter(points[:, 0], points[:, 1], c = Intensity, cmap=plt.cm.binary)
for n in range(0,Nsources):
    source1 = np.array([0,sep1[n]])
    source2 = np.array([0,sep2[n]])
    plt.scatter(*source1, c='red')
    plt.scatter(*source2, c='red')


# Intensity on the screen

d1 = np.zeros(Npoints)
d2 = np.zeros(Npoints)
wave1_screen, wave2_screen, theta = np.zeros(Npoints), np.zeros(Npoints),np.zeros(Npoints)
for n in range(0,Npoints):
    yn = y[n]
    r = np.array([xmax, yn])
    theta[n] = 360*np.arctan(yn/xmax)/(2*np.pi)
    for m in range(0,Nsources):
        source1 = np.array([0,sep1[m]])
        source2 = np.array([0,sep2[m]])
        d1 = np.linalg.norm(r-source1)
        d2 = np.linalg.norm(r-source2)
        
        wave1_screen[n] = wave1_screen[n] + A1*np.sin(k*d1)
        wave2_screen[n] = wave2_screen[n] + A2*np.sin(k*d2)


# Total wave
A = wave1_screen + wave2_screen
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