"""
Nonlinear pendulum values calculation and ploting   
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



def data_evalulation(thetaIn, omegaIn):

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

        theta_lin, omega_lin = euler(theta_lin,omega_lin,t,dt,f_lin)
        theta_non, omega_non = euler(theta_non, omega_non,t,dt,f_lin)

        theta_lin_list.append(theta_lin)
        omega_lin_list.append(omega_lin)

        theta_non_list.append(theta_non)
        omega_non_list.append(omega_non)

        t = t + dt

        nsteps += 1
        
        t_list.append(t)
        nsteps_list.append(nsteps)

    return theta_lin_list, omega_lin_list, theta_non_list, omega_non_list, nsteps_list, t_list


fig_1 = data_evalulation(0.2,0)
fig_2 = data_evalulation(1,0)
fig_3 = data_evalulation(3.14,0)
fig_4 = data_evalulation(0,1)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(fig_1[5], fig_1[0], label="Theta/steps")
ax[0, 0].plot(fig_1[5], fig_1[2], label="Theta/steps")
ax[0, 0].plot(fig_1[4], fig_1[1], label="Omega/steps")
ax[0, 0].set_title("Figure 1: Initial Conditions (0.2, 0)")
ax[0, 0].axis([0, 500, -np.pi, np.pi])

ax[0, 1].plot(fig_2[5], fig_2[0], label="Theta/steps")
ax[0, 1].plot(fig_2[5], fig_2[2], label="Theta/steps")
ax[0, 1].plot(fig_2[4], fig_2[1], label="Omega/steps")
ax[0, 1].set_title("Figure 2: Initial Conditions (1, 0)")
ax[0, 1].axis([0, 500, -np.pi, np.pi])

ax[1, 0].plot(fig_3[5], fig_3[0], label="Theta/steps")
ax[1, 0].plot(fig_3[5], fig_3[2], label="Theta/steps")
ax[1, 0].plot(fig_3[4], fig_3[1], label="Omega/steps")
ax[1, 0].set_title("Figure 3: Initial Conditions (3.14, 0)")
ax[1, 0].axis([0, 500, -np.pi, np.pi])

ax[1, 1].plot(fig_4[5], fig_4[0], label="Theta/steps")
ax[1, 1].plot(fig_4[5], fig_4[2], label="Theta/steps")
ax[1, 1].plot(fig_4[4], fig_4[1], label="Omega/steps")
ax[1, 1].set_title("Figure 4: Initial Conditions (0, 1)")
ax[1, 1].axis([0, 500, -np.pi, np.pi])

plt.tight_layout()
plt.show()
plt.axis([0, 500, -np.pi, np.pi])
plt.title(rf"$\theta$ and $\omega$ over steps")
plt.savefig(f'ex2_0-{omegaIn}_w-{thetaIn}.png')
plt.show()