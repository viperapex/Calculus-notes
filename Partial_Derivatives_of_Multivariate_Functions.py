import numpy as np
import matplotlib.pyplot as plt
import torch
import math  # for constant pi


def f(my_x, my_y):
    return my_x**2 - my_y**2


# plotting z wrt to x by varying x
xs = np.linspace(-3, 3, 1000)

# while holding y constant(e.g. y = 0)
zs_wrt_x = f(xs, 0)

# plotting
fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

plt.xlabel('x')
plt.ylabel('z')
_ = ax.plot(xs, zs_wrt_x)
plt.show()
