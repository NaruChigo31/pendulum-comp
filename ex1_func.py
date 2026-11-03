"""
Linear pendulum, but as a function to plot a few graphs
They have different initial conditions 
"""

import numpy as np
import matplotlib.pyplot as plt


k = 0
A = 0
phi = 0.66667 

def f(theta, omega, t):
    return -theta-k*omega+A*np.cos(phi*t) #assumed g/L=1

def create_plot(thetaIn, omegaIn):

    theta = thetaIn
    omega = omegaIn
    t = 0.0
    dt = 0.01
    nsteps = 0

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

    # plt.plot(nsteps_list, 0.0 * np.array(nsteps_list))
    plt.plot(nsteps_list, theta_list, label="Theta/steps")
    plt.plot(nsteps_list, omega_list, label="Omega/steps")
    plt.axis([0, 500, -np.pi, np.pi])
    plt.title(rf"$\theta$ and $\omega$ over steps")
    plt.savefig(f'ex1_0-{omegaIn}_w-{thetaIn}.png')
    plt.show()


create_plot(0.2,0)
create_plot(1,0)
create_plot(3.14,0)
create_plot(0,1)
