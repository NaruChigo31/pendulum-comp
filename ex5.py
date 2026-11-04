"""
Exercise 5
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
k = 0.5
# A = 0.9
phi = 0.66667
 
 
def f(theta, omega, t, A):
    """Eq 8c with g/L = 1 (nonlinear pendulum)."""
    return -np.sin(theta) - k * omega + A * np.cos(phi * t)
 
def rk4_step(theta, omega, t, dt, A):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t, A)
 
    k2a = dt * (omega + k1b / 2)
    k2b = dt * f(theta + k1a / 2, omega + k1b / 2, t + dt / 2, A)
 
    k3a = dt * (omega + k2b / 2)
    k3b = dt * f(theta + k2a / 2, omega + k2b / 2, t + dt / 2, A)
 
    k4a = dt * (omega + k3b)
    k4b = dt * f(theta + k3a, omega + k3b, t + dt, A)
 
    theta = theta + (k1a + 2 * k2a + 2 * k3a + k4a) / 6
    omega = omega + (k1b + 2 * k2b + 2 * k3b + k4b) / 6
    return theta, omega
 
 
# Initial values (same for both methods)
theta0 = 3
omega0 = 0
dt = 0.01
nsteps = 13000
transient = 5000
# nsteps_list = [8000, 8000, 7450, 14000, 14900]
# transient_list = [5000, 5000, 6850, 12000, 12900]
A_list = [0.9, 1.07, 1.35, 1.47, 1.5]
a_shift_list = [0.0, 0.1, 5.5, 5.5, 0]  

fig, axes = plt.subplots(3, 2, figsize=(8, 12))
axes = axes.flatten()

for ax, A, a_shift in zip(axes, A_list, a_shift_list):
    theta, omega = theta0, omega0
    t = 0.0
    
    t_list = []
    theta_list = []
    omega_list = []

    iteration_number = 0

    for i in range(nsteps):
        theta, omega = rk4_step(theta, omega, t, dt, A)
        t = t + dt

        if (np.abs(theta) > np.pi+a_shift) or (np.abs(theta) < -np.pi+a_shift):
            theta -= 2 * np.pi * np.abs(theta) / theta

        if iteration_number > transient:
            # print(f"t = {t:.2f}, theta = {theta:.4f}, omega = {omega:.4f}")
            theta_list.append(theta)
            omega_list.append(omega)
        iteration_number += 1


    ax.plot(theta_list, omega_list, ".", markersize=1, label=rf"A = {A}")
    ax.set_xlabel(r"$\theta$ (rad)")
    ax.set_ylabel(r"$\omega$ (rad/s)")
    ax.legend(loc="upper right")



axes[5].set_visible(False)
 
fig.suptitle(rf"Phase portraits, $k$=0.5, $\phi$=0.66667, $\theta(0)$={theta0}, $\omega(0)$={omega0}")
plt.tight_layout()
plt.savefig("ex5.png")
plt.show()