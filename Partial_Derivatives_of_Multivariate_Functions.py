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


def delz_delx(my_x, my_y):  # y isn't relevant for *this* partial derivative; it often would be
    return 2*my_x


# x value of interest
x_samples = [-2, -1, 0, 1, 2]

colors = ['red', 'orange', 'green', 'blue', 'purple']

# my_xs:range of x values bw 3 and -3(1000points), my_x: x value of interest, my_y: 0, my_f: function f defined earlier, fprime:derivative of interest (delz_delx), col:color


def point_and_tangent_wrt_x(my_xs, my_x, my_y, my_f, fprime, col):

    my_z = my_f(my_x, my_y)  # z as a function of x and y [z=f(x,y)]

    # Slope is partial derivatice of f(x,y) w.r.t. x
    tangent_m = fprime(my_x, my_y)
    tangent_b = my_z - tangent_m*my_x  # Line is z=mx+b, so b=z-mx
    tangent_line = tangent_m*my_xs + tangent_b

    plt.plot(my_xs, tangent_line, c=col,
             linestyle='dashed', linewidth=0.7, zorder=3)


fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

for i, x in enumerate(x_samples):
    point_and_tangent_wrt_x(xs, x, 0, f, delz_delx, colors[i])

plt.ylim(-1, 9)
plt.xlabel('x')
plt.ylabel('z', rotation=0)
_ = ax.plot(xs, zs_wrt_x)
plt.show()
