import scipy.integrate as integrate
from math import cos, sin

def curvature(x):
    return 1

def intCurvature(x):
    return integrate.quad(curvature, 0, x)

def xCoord(t):
    return integrate.quad(lambda x: cos(intCurvature(x)), 0, t)

def yCoord(t):
    return integrate.quad(lambda x: sin(intCurvature(x)), 0, t)

def curve(t):
    return [xCoord(t), yCoord(t)]
