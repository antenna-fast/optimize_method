import numpy as np
import matplotlib.pyplot as plt

# We want to calculate the root (zero point) of a function using newton-iteration
# y = x^2 + 4*x - 10

if __name__ == "__main__":
    # generate function's sample data to visualize
    ori_x = []
    ori_y = []

    for x0 in range(-100, 100):
        y0 = x0**2 + 4*x0 - 10

        ori_x.append(x0)
        ori_y.append(y0)

    # newton-iteration
    x0 = 100  # we start from 100
    y0 = x0**2 + 4*x0 - 10

    iter_x = []
    iter_y = []

    iter_x.append(x0)
    iter_y.append(y0)

    for i in range(10):
        # get new x0 at x_init: intersection
        # k = [f(x0) - 0] / [x_init - x] = f'(x0)
        #   => f'(x0) * [x_init - x] = f(x0)
        #   => f'(x0) * [x - x_init] + f(x0) = 0
        #   => [x - x_init] = -f(x0) / f'(x0)
        #   => x = x_init - f(x0) / f'(x0)

        partial_x = 2 * x0 + 4 
        
        x0 = x0 - y0 / partial_x  # get new x position

        y0 = x0**2 + 4*x0 - 10

        iter_x.append(x0)
        iter_y.append(y0)

        print("x: {}  y: {}".format(x0, y0))

    plt.scatter(ori_x, ori_y, c="r", label="Cost function")
    plt.scatter(iter_x, iter_y, c="b", label="NewtonIteration")

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Newton Get Root')
    plt.legend()

    plt.show()
