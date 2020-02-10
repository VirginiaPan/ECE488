import numpy as np
def vgp4_histogram_equalize(og_img):
    #get histogram
    hist, bins = np.histogram(og_img, bins=256, range=(0, 255), normed=None)
    #get cumsum of histogram
    cdf = np.cumsum(hist, axis=None, dtype=None, out=None)
    def func(og_img):
        #index into cumsum array to get mapped value 
        cor_img = (cdf[og_img.astype(int)]/cdf[-1]) *255
        return cor_img.astype(np.uint8)
    return func(og_img), func
    