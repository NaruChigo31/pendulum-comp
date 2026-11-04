"""
Exercise 4: Damped, driven pendulum with trapezoid and RK4 methods. Compare the two methods.
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
k = 0.5
A = 0.0
phi = 0.66667
 
 
def f(theta, omega, t):
    """Eq 8c with g/L = 1 (nonlinear pendulum)."""
    return -np.sin(theta) - k * omega + A * np.cos(phi * t)
 
def rk4_step(theta, omega, t, dt):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t)
 
    k2a = dt * (omega + k1b / 2)
    k2b = dt * f(theta + k1a / 2, omega + k1b / 2, t + dt / 2)
 
    k3a = dt * (omega + k2b / 2)
    k3b = dt * f(theta + k2a / 2, omega + k2b / 2, t + dt / 2)
 
    k4a = dt * (omega + k3b)
    k4b = dt * f(theta + k3a, omega + k3b, t + dt)
 
    theta = theta + (k1a + 2 * k2a + 2 * k3a + k4a) / 6
    omega = omega + (k1b + 2 * k2b + 2 * k3b + k4b) / 6
    return theta, omega
 
 
# Initial values (same for both methods)
theta0 = 3
omega0 = 0
dt = 0.01
nsteps_total = 3000
 
theta_trap, omega_trap = theta0, omega0
theta_rk, omega_rk = theta0, omega0
t = 0.0
 
t_list = [t]
theta_rk_list = [theta_rk]
omega_rk_list = [omega_rk]
 
for i in range(nsteps_total):
    theta_rk, omega_rk = rk4_step(theta_rk, omega_rk, t, dt)
    t = t + dt
 
    t_list.append(t)
    theta_rk_list.append(theta_rk)
    omega_rk_list.append(omega_rk)

 
plt.plot(t_list, theta_rk_list, label="Runge-Kutta 4")
plt.xlabel("Time t")
plt.ylabel(r"$\theta$ (rad)")
plt.title(r"Nonlinear pendulum, $\theta(0)=3.1415$, $\omega(0)=0$")
plt.legend()
plt.show()

plt.plot(t_list, omega_rk_list, label="Runge-Kutta 4")
plt.xlabel("Time t")
plt.ylabel(r"$\omega$ (rad/s)")
plt.title(r"Nonlinear pendulum, $\theta(0)=3.1415$, $\omega(0)=0$")
plt.legend()
plt.show()