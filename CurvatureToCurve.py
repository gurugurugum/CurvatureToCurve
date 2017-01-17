import scipy.integrate as integrate
from math import cos, sin, log, exp
import matplotlib.pyplot as plt

def curvature(x):
    return sin(x)
    # if x <= 0:
    #     return 0
    # else:
    #     return x * log(x)

def intCurvature(x):
    return integrate.quad(curvature, 0, x)[0]

def xCoord(t):
    return integrate.quad(lambda x: cos(intCurvature(x)), 0, t)[0]

def yCoord(t):
    return integrate.quad(lambda x: sin(intCurvature(x)), 0, t)[0]

def curve(t):
    return [xCoord(t), yCoord(t)]

if __name__ == '__main__':
    a = 500
    plt.plot([xCoord(i/10) for i in range(a)], [yCoord(i/10) for i in range(a)], 'b-')
    plt.show()
