"""
Linear pendulum, but as a function to plot a few graphs
They have different initial conditions 
"""

import numpy as np
import matplotlib.pyplot as plt


k = 0
A = 0
phi = 0.66667 


def f_lin(theta, omega, t):
    return -theta-k*omega+A*np.cos(phi*t) #assumed g/L=1

def f_non(theta, omega, t):
    return -np.sin(theta)-k*omega+A*np.cos(phi*t) #assumed g/L=1


def euler(theta,omega,t,dt,func):
    dtheta1 = dt * omega
    domega1 = dt * func(theta, omega, t)
    dtheta2 = dt * (omega + domega1)
    domega2 = dt * func(theta + dtheta1, omega + domega1, t + dt)

    theta = theta + (dtheta1 + dtheta2) / 2
    omega = omega + (domega1 + domega2) / 2
    # t = t + dt    

    return theta, omega



def create_plot(thetaIn, omegaIn):

    theta_lin = thetaIn
    theta_non = thetaIn
    omega_lin = omegaIn
    omega_non = omegaIn
    t = 0.0
    dt = 0.01
    nsteps = 0

    theta_lin_list = [theta_lin]
    omega_lin_list = [omega_lin]

    theta_non_list = [theta_non]
    omega_non_list = [omega_non]

    nsteps_list = [nsteps] # np.arange(0, 1000)
    t_list = [t]

    for i in range(1000):
        # non linear part
        dtheta1 = dt * omega
        domega1 = dt * f_lin(theta, omega, t)
        dtheta2 = dt * (omega + domega1)
        domega2 = dt * f_lin(theta + dtheta1, omega + domega1, t + dt)

        theta = theta + (dtheta1 + dtheta2) / 2
        omega = omega + (domega1 + domega2) / 2


        t = t + dt

        nsteps += 1

        theta_lin, omega_lin = euler(theta_lin,omega_lin,t,dt,f_lin)
        theta_non, omega_non = euler(theta_non, omega_non,t,dt,f_lin)

        theta_lin_list.append(theta_lin)
        omega_lin_list.append(omega_lin)

        theta_non_list.append(theta_non)
        omega_non_list.append(omega_non)

        t_list.append(t)
        nsteps_list.append(nsteps)

    # plt.plot(nsteps_list, 0.0 * np.array(nsteps_list))
    plt.plot(t_list, theta_lin_list, label="Theta/steps")
    plt.plot(t_list, theta_non_list, label="Theta/steps")
    plt.plot(nsteps_list, omega_lin_list, label="Omega/steps")
    plt.axis([0, 500, -np.pi, np.pi])
    plt.title(rf"$\theta$ and $\omega$ over steps")
    plt.savefig(f'ex1_9__0-{omegaIn}_w-{thetaIn}.png')
    plt.show()


create_plot(0.2,0)
create_plot(1,0)
create_plot(3.14,0)
create_plot(0,1)
