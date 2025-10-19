import numpy as np
import matplotlib.pyplot as plt

# range of x values (100 data points evenly spaced) start, finish, n points
x = np.linspace(-10, 10, 1000)

# passing the 1000 x values into a function that will
# give us a 1000 outputs y which we can use (1000x and 1000y values) to plot a curve
y = x**2 + 2*x + 2

fig, ax = plt.subplots()
_ = ax.plot(x, y)
plt.show()


# zooming in infinitely closely we observe curves that approach lines.
# this enables us to find the slope m(tangent) anywhere on the curve.
fig, ax = plt.subplots()
ax.set_xlim([-1.5, -0.5])
ax.set_ylim([0.5, 1.5])
_ = ax.plot(x, y)
plt.show()


# we zoom more
fig, ax = plt.subplots()
ax.set_xlim([-1.1, -0.9])
ax.set_ylim([0.9, 1.1])
_ = ax.plot(x, y)
plt.show()

# we zoom even more
fig, ax = plt.subplots()
ax.set_xlim([-1.01, -0.99])
ax.set_ylim([0.99, 1.01])
_ = ax.plot(x, y)
plt.show()
