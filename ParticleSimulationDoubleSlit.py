# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:27:06 2022

@author: Ariel Norambuena
"""

import numpy as np
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt
import time

start_time = time.time()


def main():
    """ Double slit simulation """
    ## Geometrical parameters
    a = 3;             # slit length
    d = 6*a;           # distance between slits
    Lb = 2*d;          # distance between box and slits
    ws = a;            # slit width
    Ls = 5*d;         # distance between slit and screen
    wb = d+a/2;        # box width
    Lx = Lb+Ls+ws;     # total length along x direction for simulation
    Ly = 4*wb;         # total length along y direction for simulation
    
    ## Physical parameters
    F = 100;                # factor to reduce velocity along y direction, vy=vx/F
    v0 = 50;                # mean velocity along x direction
    dt = 0.1*ws/v0;         # step time
    Np = 100;               # number of particles
    Nt = 1000;              # number of iterations of time dt
    Error = v0*dt;          # size errror
    qe = 1.6e-19;           # electron charge
    me = 9.1e-31;           # electron mass
    ke = 9e+3;              # Coulomb constant, kg*(micro meter)^3/(ps)^2
    F0 = ke*(qe)**2;        # force factor for Coulomb interaction
    
    # Animation 
    plotRealTime = True
    
    # Initial position for Np particles
    xi, xf = -wb, 0
    x = (xf-xi)*np.random.rand(1,Np) + xi
    yi, yf = -0.5*(d+a), 0.5*(d+a)
    y = (yf-yi)*np.random.rand(1,Np) + yi
    
    
    # Initial velocity for Np particles
    dv = v0/5
    vxi, vxf = v0-dv, v0+dv
    vx = (vxf-vxi)*np.random.rand(1,Np) + vxi
    
    dv = v0/F
    vyi, vyf = -dv, dv
    vy = (vyf-vyi)*np.random.rand(1,Np) + vyi
    
    # Initial forces
    Fx = np.zeros((1,Np))
    Fy = np.zeros((1,Np))
    
    
    # Prep figure
    fig = plt.figure(figsize=(4,4), dpi=100)
    ax = plt.gca()

    
    
    # Simulation of particles
    for n in range(0,Nt):    
       
        # Force
        X = x-np.transpose(x);
        Y = y-np.transpose(y);
        R = np.sqrt(X**2+Y**2+Error**2);
    
        # Forces
        FX = F0*X/R**3 
        FY = F0*Y/R**3 
    
        for i in range(0,Np):
            Fx[:,i] = -np.sum(FX[:,i])
            Fy[:,i] = -np.sum(FY[:,i])
            
                    
        ## Update velocities
        vx = vx + Fx*dt/me;
        vy = vy + Fy*dt/me;
                     
        ## Update positions
        x = x + vx*dt;
        y = y + vy*dt;
               
                    
        # Collision with walls
        for i in range(0,Np):
            # Region I
            if x[:,i]+Error > Lb and x[:,i]-Error < Lb+ws and y[:,i]+Error > (d+a)/2:
                vx[:,i] = - vx[:,i]
            
            # Region II
            if x[:,i]-Error < Lb+ws and x[:,i]+Error > Lb and y[:,i]+Error > (d+a)/2:
                vy[:,i] = - vy[:,i]
            elif x[:,i]-Error < Lb+ws and x[:,i]+Error > Lb and y[:,i]-Error < (d-a)/2:
                vy[:,i] = - vy[:,i]
            
            # Region III
            if x[:,i]+Error > Lb and x[:,i]-Error < Lb+ws  and y[:,i]+Error > (a-d)/2 and y[:,i]-Error <(d-a)/2:
                vx[:,i] = - vx[:,i]
            
            # Region IV
            if x[:,i]-Error < Lb+ws and x[:,i]+Error > Lb and y[:,i]+Error > (a-d)/2:
                vy[:,i] = - vy[:,i]
            elif x[:,i]-Error < Lb+ws and x[:,i]-Error > Lb and y[:,i]-Error < -(d+a)/2:
                vy[:,i] = - vy[:,i]
            
            # Region V
            if x[:,i]+Error > Lb and x[:,i]-Error < Lb+ws and y[:,i]-Error < -(a+d)/2:
                vx[:,i] = - vx[:,i]
            
            # Collision with scren
            if x[:,i]+Error>=Lx:
                vx[:,i] = 0
                vy[:,i] = 0
        
        
        ## Update velocities
        vx = vx + Fx*dt/me;
        vy = vy + Fy*dt/me;
                     
        ## Update positions
        x = x + vx*dt;
        y = y + vy*dt;
        
        if plotRealTime or (i == Nt-1):
            plt.cla()
            plt.plot(x,y, 'o', color='black');
            plt.xlim(-wb,Lx)
            plt.ylim(-Ly/2,Ly/2)
            ax.set_aspect('equal')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            # Double slit
            # Left 
            x1, y1 = Lb, d/2+a/2
            x2, y2 = Lb, Ly/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb, -(d/2-a/2)
            x2, y2 = Lb, (d/2-a/2)
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb, -(d/2+a/2)
            x2, y2 = Lb, -Ly/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            # Right 
            x1, y1 = Lb+ws, d/2+a/2
            x2, y2 = Lb+ws, Ly/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb+ws, -(d/2-a/2)
            x2, y2 = Lb+ws, (d/2-a/2)
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb+ws, -(d/2+a/2)
            x2, y2 = Lb+ws, -Ly/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            # Middle
            x1, y1 = Lb, d/2+a/2
            x2, y2 = Lb+ws, d/2+a/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb, d/2-a/2
            x2, y2 = Lb+ws, d/2-a/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lb, -(d/2-a/2)
            x2, y2 = Lb+ws, -(d/2-a/2)
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            x1, y1 = Lx, -Ly/2
            x2, y2 = Lx, Ly/2
            plt.plot((x1, x2), (y1, y2), 'k-') 
            
            ## Screen
            x1, y1 = Lb, -(d/2+a/2)
            x2, y2 = Lb+ws, -(d/2+a/2)
            plt.plot((x1, x2), (y1, y2), 'k-')
            
            plt.pause(dt)
    

    plt.show()        
    
    return 0

if __name__== "__main__":
  main()
print("--- %s seconds ---" % (time.time() - start_time))