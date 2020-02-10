import numpy as np

def capture(fcn, T, D, g, t_0=0):
    #get t values at 1GHz sampling rate
    t = np.arange(t_0, t_0+T, 1/(1*10**9))
    # calculate f(t) values
    f_t = fcn(t)
    energy = (D/2)**2*np.pi*(1/683)*np.trapz(f_t, x=None, dx=1/(1*10**9), axis=0)
    voltage = g*np.sqrt(2*energy/1)
    disc = round(voltage, 0)
    if (disc>255):
        return 255
    elif(disc<0):
        return 0
    else:
        return int(disc)

if __name__ == '__main__':
    def make_fcn(x):
        return 0.5*np.sin(x)+0.5
    print(capture(make_fcn, 0.001, 5, 100))