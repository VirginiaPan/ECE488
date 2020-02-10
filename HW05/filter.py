#filter.py

import numpy as np
import matplotlib.pyplot as plt


def filter1(x, h):
    """Convolve 1D arrays."""
    # pad x with zeros
    wing = np.zeros((int((h.size - 1) / 2),))
    _x = np.concatenate((wing, x, wing), axis=0)
    y = np.zeros(x.shape)
    for i in range(x.size):
        for u in range(h.size):
            y[i] += _x[i + u] * h[u]
    return y

def filter2(x, h):
    """Convolve 2D arrays."""
    # pad x with zeros
    [im_height, im_width] = x.shape
    [h_height, h_width] = h.shape
    
    wingW = np.zeros((im_height, int((h_width - 1) / 2))) # width
    _x = np.concatenate((wingW, x, wingW), axis=1)

    wingH = np.zeros((int((h_height - 1) / 2), _x.shape[1])) #height
    _x = np.concatenate((wingH, _x, wingH), axis=0)

    out = np.zeros(x.shape)

    for i in range(im_height):
        for j in range(im_width):
            for u in range(h.shape[0]):
                for v in range(h.shape[1]):
                    out[i,j] += _x[i + u, j + v] * h[u,v]
    
    return out


def filter2sep(x, h1, h2):
    filter2(filter2(x, h1), h2)

x = np.ones((9,9))
# h = np.random.random(size=(3,3))
# filter2(x,h)

h1 = np.random.random(size=(3,1))
h2 = np.random.random(size=(1,3))
filter2sep(x, h1, h2)

if __name__ == "__main__":
    N = 100
    n = 11
    i = np.linspace(0, 2 * np.pi, N)
    x = np.sin(i * 4) + np.sin(i * 25)
    h = np.ones((n,)) / n
    y = filter1(x, h)
    plt.plot(x)
    plt.plot(y)
    plt.show()