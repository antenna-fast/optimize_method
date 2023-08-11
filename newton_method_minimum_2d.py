import numpy as np
import time
import matplotlib.pyplot as plt

# 2-Dim Newton

# z = x^2 + y^2 + x + y + xy + 1
# partial x = 2*x + y + 1
# partial y = 2*y + x + 1

x0 = [1, 1]  # init point

p_x = 2*x0[0] + x0[1] + 1
p_y = 2*x0[1] + x0[0] + 1

p_xx = 2
p_yy = 2
p_xy = 1
p_yx = 1

g0 = [p_x, p_y]
g0_norm = np.linalg.norm(g0)

H0 = np.array([[p_xx, p_xy],
               [p_yx, p_yy]
               ])

print('H0:\n', H0)

# pts = [x0]
pts = []
z = []

while g0_norm > 0.01:
    # print(g0_norm)

    x0 = x0 - 0.1 * np.dot(np.linalg.inv(H0), g0)  # update x0
    # print('x0:', x0)
    pts.append(x0)

    # update g0 partial x/y (Jacobin)
    p_x = 2 * x0[0] + x0[1] + 1
    p_y = 2 * x0[1] + x0[0] + 1
    g0 = [p_x, p_y]
    g0_norm = np.linalg.norm(g0)  # don't forget to update end_condition!
    print('g0: ', g0)

    # this case, H is constant!

    # check y
    y = x0[0]**2 + x0[1]**2 + x0[0] + x0[1] + x0[0]*x0[1] + 1
    print('y: ', y)
    z.append(z)
    time.sleep(0.01)  # fastidium delay...
