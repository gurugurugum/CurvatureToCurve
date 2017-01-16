import scipy.integrate as integrate
from math import cos, sin, log, exp

def curvature(x):
    return exp(x)
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
