import numpy as np
import time
import matplotlib.pyplot as plt
import visdom

# find the minimum of y
# y = x^2 + x + 1
# y' = 2x + 1
# y'' = 2

x0 = 91.91

g = 2*x0 + 1  # f'(x0)
gg = 2  # f''(x0)

while abs(g) > 0.001:
    # update x0
    x0 = -g/gg + x0

    # update one order partial
    g = 2*x0 + 1

    # update two order partial, will, in this case it is constant
    gg = 2

    print(g)

y = x0**2 + x0 + 1
print('\nx_final is {0}, and min_y is {1}'.format(x0, y))


#  2-Dim Newton
# z = x^2 + y^2 + x + y + xy + 1
# partial x = 2*x + y + 1
# partial y = 2*y + x + 1

x0 = [1, 1]  # nit point

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

    # update g0 sprct partail x/y
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

# pts = np.array(pts).T
# # print(x0.shape)
# print('pts:', pts)
# plt.scatter(pts[0], pts[1], marker='*')
# plt.show()
