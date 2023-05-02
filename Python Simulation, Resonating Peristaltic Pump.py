#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from scipy.integrate import odeint
from scipy import signal
import matplotlib.pyplot as plt

# Initialization
tstart = 0
Amp = 5
tstop = 4
Step = 0.004

# Initial conditions
x_init = [0,0]
t = np.arange(tstart,tstop+1,step)

# Create the equation of motion
def mydiff(x, t):
    c = 5.47# Coefficient of Damping
    k = 202.7  # Coefficient of Stiffness
    m = 0.075  # Mass of the pincher assembly
    F = 0.5*2300*(signal.square(2 * np.pi * Amp*(t)) +1)
    dx1dt = x[1]
    dx2dt = (F/m - c/m*x[1] - k/m*x[0])
    dxdt = [dx1dt, dx2dt]
    return dxdt

# Solve the equation of motion
x = odeint(mydiff, x_init, t)
x1 = x[:,0]

# Plot Figure
plt.plot(t,x1)
plt.title('6.25Hz 1DOF Simulation of MSD System')
plt.xlim(0,5)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#print the x & y coordinates
#print(x1)
#print(t)

