import numpy as np
import matplotlib.pylab as plt

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

x = np.array([1, 1, 4])
print (softmax(x))

x = np.array([1100, 1090, 1011])
print (softmax(x))