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


def trapezoid(theta,omega,t,dt,func):
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

        theta_lin, omega_lin = trapezoid(theta_lin,omega_lin,t,dt,f_lin)
        theta_non, omega_non = trapezoid(theta_non, omega_non,t,dt,f_non)

        theta_lin_list.append(theta_lin)
        omega_lin_list.append(omega_lin)

        theta_non_list.append(theta_non)
        omega_non_list.append(omega_non)

        t = t + dt

        nsteps += 1
        
        t_list.append(t)
        nsteps_list.append(nsteps)

    return theta_lin_list, omega_lin_list, theta_non_list, omega_non_list, nsteps_list, t_list


# fig_1 = data_evalulation(0.2,0)
# fig_2 = data_evalulation(1,0)
# fig_3 = data_evalulation(3.14,0)
# fig_4 = data_evalulation(0,1)

# fig, ax = plt.subplots(2, 2)

fig, ax = plt.subplots(4, 2, figsize=(8, 12))

conditions = [(0.2, 0), (1, 0), (3.14, 0), (0, 1)]

for row, (theta0, omega0) in enumerate(conditions):
    th_l, om_l, th_n, om_n, steps, t = data_evalulation(theta0, omega0)

    for col, (lin, non, ylabel) in enumerate([(th_l, th_n, "theta"), (om_l, om_n, "omega")]):
        a = ax[row, col]
        a.plot(t, lin, label="Linear")
        a.plot(t, non, label="Nonlinear")
        a.plot([], [], ' ', label=rf"$\theta(0)$={theta0}")
        a.plot([], [], ' ', label=rf"$\omega(0)$={omega0}")
        a.set_xlabel("t")
        a.set_ylabel(ylabel)
        a.legend(loc="upper right")

plt.tight_layout()
plt.savefig("ex2_all.png")
plt.show()