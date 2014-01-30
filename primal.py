#!/usr/bin/env python

###########################################################################
# Name: Evan Chow
# Date: 12/2013-1/2013
# Contact: echow4@outlook.com
# Course project? no
# Description: Implementation of primal form of perceptron. Will push dual
#   dual form later, which is still buggy.
# Python packages used: NumPy, Matplotlib
# How to run: $ python primal.py
###########################################################################

import numpy as np 
from math import copysign
import matplotlib.pyplot as plt

class primal():

    # plot all points for initial exploration
    def plotAll(self, x,y):
        for i in xrange(len(x)):
            if y[i] == 1:
                plt.scatter(x[i,0],x[i,1],color='g')
            else:
                plt.scatter(x[i,0],x[i,1],color='r')

    # Primal implementation of the perceptron algorithm.
    def __init__(self, n, w, b, r, x, y):
        def sgn(w,xi,b,yi):
            result = np.dot(w, xi) - b
            if copysign(1, result) != yi:
                return False
            return True
        length = len(x)
        while True:
            for i in xrange(length):
                if sgn(w, x[i], b, y[i]) is False:
                    w = w + n * y[i] * x[i]
                    b = b - n * y[i] * (r**2)
            gen = (1 if sgn(w, x[j], b, y[j]) is True 
                else 0 for j in xrange(length))
            if all(g == 1 for g in gen):
                break
        self.w = w
        self.b = b

    # Return weights and bias. Still buggy.
    def wb(self):
        return self.w, self.b

    # Plot primal separator line.
    # x1 and x2's default values are 1 and 9.
    def plot_boundary(self, x1=1, x2=9):
        z1 = (1 / self.w[1]) * (self.b - self.w[0]*x1)
        z2 = (1 / self.w[1]) * (self.b - self.w[0]*x2)
        plt.plot([x1, x2],[z1,z2])

if __name__=="__main__":
    # sample data. classes = +1, upper right; -1, lower left
    x = np.array([[1,1],[2,2],[3,3],[2,5],[7,3],[8,1],[4,4],[5,5],[2,6],[2,4],[3,7]])
    y = np.array([1,1,1,1,1,1,1,-1,-1,1,-1])
    length = len(x)

    # Initialize n, w, b, r for perceptron
    n = 0.2
    w = np.array([0,0]) # initial
    b = 0
    r = 0
    for i in xrange(length):
        mag = np.linalg.norm(x[i])
        if r < mag:
            r = mag

    # Initiate and plot perceptron
    percept = primal(n, w, b, r, x, y)
    print "Primal values (w, b): %s, %s" % (percept.wb())
    percept.plotAll(x, y)
    percept.plot_boundary()
    plt.show()