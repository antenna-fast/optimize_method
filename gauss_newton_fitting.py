import numpy as np

# ref: https://zhuanlan.zhihu.com/p/42383070

# Jacobin
# M functions, N vars
# the Jacobin matrix shape is MxN
# each row represent N var's partial of one function

# y = a*x^2 + b*x + c
# gt: a=1, b=2, c=3

# we can also represent it as "residual" in cost function (residual = f(x) - 0)
def get_val(x):
    y = x*x + 2*x + 3
    return y

def f(p, x):
    y = p[0]*x*x + p[1]*x + p[2]
    return y

def get_jacobin(x):
    J = np.array([x*x, x, 1]).reshape(1, 3)
    return J


if __name__ == "__main__":
    print("gauss-newton demo")
    # step 1: calculate Jacobin
    # step 2: calculate /Delta x by solving linear function (increment)
    # step 3: iteration until 

    p = np.array([15, 1.0, 100]).reshape(3, 1)  # a, b, c
    
    for j in range(3):
        JTJ = np.zeros((3, 3))
        JTr = np.zeros((3, 1))

        for x in np.arange(-100, 100, 0.05):
            y = get_val(x)  # generate train data
            yy = f(p, x)

            r = yy - y

            J = get_jacobin(x)
            JT = J.reshape(3, 1)
            JTJ += np.dot(JT , J)
            JTr += JT*r

        # print("JT: \n", JT)
        # print("JTJ: \n", JTJ)
        delta_x = np.linalg.solve(JTJ, -JTr)
        # print(delta_x)
        p += delta_x

        print("p: ", p)
