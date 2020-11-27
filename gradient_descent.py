import numpy as np

# y = x^2 + x + 1
x0 = 1  # start with x0
lama = 0.1  # lamada

g = 2*x0 + 1

# kernel function
while abs(g) > 0.001:  # partial x > a very very small epsilon, iterate it
    g = 2*x0 + 1  # update rtial x
    x0 = x0 - lama*g  # update x0
    print(g)

y = x0**2 + x0 + 1
print('\nx_final is {0}, and min_y is {1}'.format(x0, y))
