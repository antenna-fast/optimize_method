import numpy as np
import scipy as sp
import matplotlib.pyplot as pt
import scipy.linalg as la

# f(t)=x0*e^(x1*t)
 
t = np.array([0.0, 1.0, 2.0, 3.0])
y = np.array([2.0, 0.7, 0.3, 0.1])

# First, define a residual function (as a function of 
def residual(x):
    return y - x[0] * np.exp(x[1] * t)

def jacobian(x):
    return np.array([
        -np.exp(x[1] * t),  # partial x0
        -x[0] * t * np.exp(x[1] * t)  # partial x1
        ]).T

J = jacobian(np.array([1, 0]))
print(J)

# def plot_guess(x):
#     pt.plot(t, y, 'ro', markersize=20, clip_on=False)
#     T = np.linspace(t.min(), t.max(), 100)
#     Y = x[0] * np.exp(x[1] * T)
#     pt.plot(T, Y, 'b-')
    
#     print("Residual norm:", la.norm(residual(x), 2))

# plot_guess(x)
