
import math
import numpy as np

from typing import List, Union

def _5dec(num):
    return int(num * 100000) / 100000

# ---------------------------------------------- #

def _6dec(num):
    return int(num * 1000000) / 1000000


# flipping matrices

# flipping matrices
# goal is to calculate for first matrix
# right now, all I need to do is collect first 
# 100 values, take first 2 and last 2, output 
# some matrix with correct values

# sample on docs btw

# load data
with open("righthand", 'r') as file:
    data = file.read()
    file.close()

parsed = [tuple(map(float, x.split())) for x in data.split('\n')]

# numpy.tranpose to transpose

def find_quartic(parsed):
    datasize = len(parsed)
    # now we have a parsed list of coordinate values
    # create matrix - X
    X = np.array([[1.0, parsed[i][0], parsed[i][0]**2, parsed[i][0]**3, parsed[i][0]**4] for i in range(datasize)], dtype=np.double)
    # and vector - Y
    Y = np.array([parsed[i][1] for i in range(datasize)], dtype=np.double)

    # for i in range(2):
    #     print("&".join([str(_6dec(X[i][0])), str(_6dec(X[i][1])), str(_6dec(X[i][2])), str(_6dec(X[i][-2])), str(_6dec(X[i][-1]))]) + "\\\\")
    # print("...&"*4+"...\\\\")
    # for i in range(datasize-2, datasize):
    #     print("&".join([str(_6dec(X[i][0])), str(_6dec(X[i][1])), str(_6dec(X[i][2])), str(_6dec(X[i][-2])), str(_6dec(X[i][-1]))]) + "\\\\")


    XT = np.transpose(X)

    # print(np.shape(XT))
    # for i in range(5):
    #     print("&".join([str(_6dec(XT[i][0])), str(_6dec(XT[i][1])), "...", str(_6dec(XT[i][-2])), str(_6dec(XT[i][-1]))]) + "\\\\")

    # # next solve for XT*X
    XT_X = np.matmul(XT, X)

    # print(np.shape(XT_X))
    # for i in range(5):
    #     print("&".join([str(_6dec(XT_X[i][0])), str(_6dec(XT_X[i][1])), "...", str(_6dec(XT_X[i][-2])), str(_6dec(XT_X[i][-1]))]) + "\\\\")


    iXT_X = np.linalg.inv(XT_X)
    # print(np.shape(iXT_X))
    # for i in range(5):
    #     print("&".join([str(_6dec(iXT_X[i][0])), str(_6dec(iXT_X[i][1])), "...", str(_6dec(iXT_X[i][-2])), str(_6dec(iXT_X[i][-1]))]) + "\\\\")


    coef = np.matmul(np.matmul(iXT_X, XT), Y)
    return coef
    # print([float(x) for x in coef])


def find_cubic(parsed):
    datasize = len(parsed)
    # now we have a parsed list of coordinate values
    # create matrix - X
    X = np.array([[1.0, parsed[i][0], parsed[i][0]**2, parsed[i][0]**3] for i in range(datasize)], dtype=np.double)
    # and vector - Y
    Y = np.array([parsed[i][1] for i in range(datasize)], dtype=np.double)

    # for i in range(2):
    #     print("&".join([str(_6dec(X[i][0])), str(_6dec(X[i][1])), str(_6dec(X[i][2])), str(_6dec(X[i][-2])), str(_6dec(X[i][-1]))]) + "\\\\")
    # print("...&"*4+"...\\\\")
    # for i in range(datasize-2, datasize):
    #     print("&".join([str(_6dec(X[i][0])), str(_6dec(X[i][1])), str(_6dec(X[i][2])), str(_6dec(X[i][-2])), str(_6dec(X[i][-1]))]) + "\\\\")


    XT = np.transpose(X)

    # print(np.shape(XT))
    # for i in range(5):
    #     print("&".join([str(_6dec(XT[i][0])), str(_6dec(XT[i][1])), "...", str(_6dec(XT[i][-2])), str(_6dec(XT[i][-1]))]) + "\\\\")

    # # next solve for XT*X
    XT_X = np.matmul(XT, X)

    # print(np.shape(XT_X))
    # for i in range(5):
    #     print("&".join([str(_6dec(XT_X[i][0])), str(_6dec(XT_X[i][1])), "...", str(_6dec(XT_X[i][-2])), str(_6dec(XT_X[i][-1]))]) + "\\\\")


    iXT_X = np.linalg.inv(XT_X)
    # print(np.shape(iXT_X))
    # for i in range(5):
    #     print("&".join([str(_6dec(iXT_X[i][0])), str(_6dec(iXT_X[i][1])), "...", str(_6dec(iXT_X[i][-2])), str(_6dec(iXT_X[i][-1]))]) + "\\\\")


    coef = np.matmul(np.matmul(iXT_X, XT), Y)
    return coef
    # print([float(x) for x in coef])



find_quartic(parsed)

print(f"{parsed[0]:.6f} +")
print(" ".join([f"{x:.6f}" for x in find_quartic(parsed)]))

