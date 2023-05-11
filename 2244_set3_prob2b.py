import numpy as np
import matplotlib.pyplot as plt

# This function recursively calculates the probability that all of the
# leaves fail.  When n = 1, the value would only be f^2 becuase the rest
# of the function would become 0.
def calc_z(n, f):
    z = 0
    if n == 1:
        return z + f**2
    elif n > 1:
        return z + ((f**2) + ((2*f) * (1-f) * calc_z(n-1, f))\
             + ((1-f)**2 * calc_z(n-1, f)))
    else:
        return z

#Plot Setup
plt.title("Probability of All Leaves Failing with changing f")
plt.xlabel("Probability f")
plt.ylabel("Probability of All Leaves Failing")
f = np.arange(0, 1, 0.01)
y = (1 - (1-f)**2)**4 #calculates probabilities if leaves were independent
z = calc_z(2, f)
plt.plot(f, y, label="Function with Independence")
plt.plot(f, z, label="Function with Dependence")
#show plot
plt.legend()
plt.show()
