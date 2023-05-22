import numpy as np 

def map_feature(X1, X2):
#   Returns a new feature array with more features, comprising of 
#   x1, x2, x1.^2, x2.^2, x1*x2, x1*x2.^2, etc.
    degree = 6
    X1 = np.atleast_1d(X1)
    X2 = np.atleast_1d(X2)
    out = []
    for i in range(1, degree+1):
        for j in range(i + 1):
            out.append((X1**(i-j) * (X2**j)))
    return np.stack(out, axis=1)