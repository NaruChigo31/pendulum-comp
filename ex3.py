"""
Exercise 3: nonlinear pendulum solved with two integrators.
Compares the trapezoid rule (eqs 12a/12b) with fourth order Runge-Kutta
for theta(0) = 3.1415, omega(0) = 0.0, and plots theta versus time for both
methods on one graph.
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
k = 0.0
A = 0.0
phi = 0.66667
 
 
def f(theta, omega, t):
    """Eq 8c with g/L = 1 (nonlinear pendulum)."""
    return -np.sin(theta) - k * omega + A * np.cos(phi * t)
 
 
def trapezoid_step(theta, omega, t, dt):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt)
 
    theta = theta + (k1a + k2a) / 2
    omega = omega + (k1b + k2b) / 2
    return theta, omega
 
 
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
theta0 = 3.1415
omega0 = 0.0
dt = 0.01
nsteps_total = 12000
 
theta_trap, omega_trap = theta0, omega0
theta_rk, omega_rk = theta0, omega0
t = 0.0
 
t_list = [t]
theta_trap_list = [theta_trap]
theta_rk_list = [theta_rk]
 
for i in range(nsteps_total):
    theta_trap, omega_trap = trapezoid_step(theta_trap, omega_trap, t, dt)
    theta_rk, omega_rk = rk4_step(theta_rk, omega_rk, t, dt)
    t = t + dt
 
    t_list.append(t)
    theta_trap_list.append(theta_trap)
    theta_rk_list.append(theta_rk)
 
plt.plot(t_list, theta_trap_list, label="Trapezoid rule")
plt.plot(t_list, theta_rk_list, label="Runge-Kutta 4")
plt.xlabel("Time t")
plt.ylabel(r"$\theta$ (rad)")
plt.title(r"Nonlinear pendulum, $\theta(0)=3.1415$, $\omega(0)=0$")
plt.legend()
plt.show()