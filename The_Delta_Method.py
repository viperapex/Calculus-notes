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
_ = ax.plot(x, y)
plt.show()


# Indentifying what the slope is at x

print(f(2))
