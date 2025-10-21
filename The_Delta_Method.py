import numpy as np
import matplotlib.pyplot as plt

# range of x values (100 data points evenly spaced) start, finish, n points
x = np.linspace(-10, 10, 1000)

y = x**2 + 2*x + 2


def f(my_x):
    my_y = my_x**2 + 2*my_x + 2
    return my_y


y = f(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)  # new
plt.scatter(5, 37, c='orange', zorder=3)  # new
_ = ax.plot(x, y)
plt.show()


# Indentifying what the value of y is at x
z = f(2)
print(z)
