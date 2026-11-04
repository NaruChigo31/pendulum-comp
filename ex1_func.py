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

def create_plot(ax, thetaIn, omegaIn):

    theta = thetaIn
    omega = omegaIn
    t = 0.0
    dt = 0.01
    nsteps = 0

    theta_list = [theta]
    omega_list = [omega]
    nsteps_list = [nsteps]

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

    ax.plot(nsteps_list, theta_list, label=r"$\theta$")
    ax.plot(nsteps_list, omega_list, label=r"$\omega$")
    ax.plot([], [], ' ', label=rf"$\theta(0)$={thetaIn}, $\omega(0)$={omegaIn}")
    ax.axis([0, 500, -np.pi, np.pi])
    ax.set_xlabel("nsteps")
    ax.set_ylabel(r"$\theta$, $\omega$")
    ax.legend(loc="upper right")


fig, ax = plt.subplots(2, 2, figsize=(8, 6))

create_plot(ax[0, 0], 0.2, 0)
create_plot(ax[0, 1], 1, 0)
create_plot(ax[1, 0], 3.14, 0)
create_plot(ax[1, 1], 0, 1)

fig.suptitle(r"Linear pendulum: $\theta$ and $\omega$ over steps")
plt.tight_layout()
plt.savefig("ex1_all.png")
plt.show()