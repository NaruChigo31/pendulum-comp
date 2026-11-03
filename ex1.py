"""
Linear pendulum values calculation and ploting using euler method?
"""

import numpy as np
import matplotlib.pyplot as plt

theta = 0.2
omega = 0.0
t = 0.0
dt = 0.01
nsteps = 0


k = 0
A = 0
phi = 0.66667 

def f(theta, omega, t):
    # return (-g/L)*np.sin(theta)-k*omega+A*np.cos(phi*t)
    return -theta-k*omega+A*np.cos(phi*t) #assumed g/L=1

# initial f was literaly "-theta" as k,A=0
print(f(1,2,3)) #-1
print(f(3,2,3)) #-3


theta_list = [theta]
omega_list = [omega]
nsteps_list = [nsteps] # np.arange(0, 1000)

for i in range(1000):
    dtheta1 = dt * omega
    domega1 = dt * f(theta, omega, t)
    dtheta2 = dt * (omega + domega1)
    domega2 = dt * f(theta + dtheta1, omega + domega1, t + dt)

    theta = theta + (dtheta1 + dtheta2) / 2
    omega = omega + (domega1 + domega2) / 2
    t = t + dt

    nsteps += 1

    theta_list.append(theta)
    omega_list.append(omega)
    nsteps_list.append(nsteps)



    # if i>998:
    #     print(i)


print(theta, omega) # 0.19999 -0.002
print(nsteps)
# improved to -0.1677963797371138 0.10883232491885439

# plt.plot(nsteps_list, 0.0 * np.array(nsteps_list))
plt.plot(nsteps_list, theta_list, label="Theta/steps")
plt.plot(nsteps_list, omega_list, label="Omega/steps")
plt.axis([0, 500, -np.pi, np.pi])
plt.title(rf"$\theta$ and $\omega$ over steps")
plt.show()
