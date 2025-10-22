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
plt.scatter(2, 10)  # Point P
plt.scatter(5, 37, c='orange', zorder=3)  # Point Q
_ = ax.plot(x, y)
plt.show()


# Indentifying what the value of y is at x
z = f(2)
print(z)


# Finding the slope m between points P and Q
m = (37-10)/(5-2)
print(m)

# To plot the line that passes through P and Q , We can rearrange the equation of a line y = mx+b:
b = 37-m*5
print(b)


line_y = m*x+b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)  # Point P
plt.scatter(5, 37, c='orange', zorder=3)  # Point Q
plt.ylim(-5, 150)
plt.plot(x, line_y, c='orange')
_ = ax.plot(x, y)
plt.show()

e = f(2.1)
print(e)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2, 10)  # Point P
plt.scatter(2.1, 10.61, c='orange', zorder=3)  # Point Q
_ = ax.plot(x, y)
plt.show()

m = (10.61-10)/(2.1-2)
print(m)

b = 10.61-m*2.1
print(b)

line_y = m*x + b


# The closer Q becomes to P(i.e. delta x approaches 0) it becomes clearer that
# the slope m at point P = (2, 10) is equal to 6
fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2.1, 10)  # Point P
plt.scatter(2.1, 10.61, c='orange', zorder=3)  # Point Q
plt.ylim(-5, 150)
plt.plot(x, line_y, c='orange', zorder=3)
_ = ax.plot(x, y)
plt.show()


delta_x = 0.000001
print(delta_x)

x1 = 2
y1 = 10

x2 = x1 + delta_x
print(x2)

y2 = f(x2)
print(y2)

m = (y2 - y1)/(x2 - x1)
print(m)


x1 = -1

y1 = f(x1)
print(y1)

print(delta_x)


x2 = x1 + delta_x
print(x2)

y2 = f(x2)
print(y2)

y2 = f(x1 + delta_x)
print(y2)

m = (y2-y1)/(x2-x1)
print(m)

b = y2-m*x2
print(b)

line_y = m*x + b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(x1, y1)  # Point P
plt.scatter(x2, y2, c='orange', zorder=3)  # Point Q
plt.ylim(-5, 150)
plt.plot(x, line_y, c='orange', zorder=3)
_ = ax.plot(x, y)
plt.show()


def diff_demo(my_f, my_x, my_delta):
    return (my_f(my_x + my_delta) - my_f(my_x)) / my_delta


deltas = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

for delta in deltas:
    print(diff_demo(f, 2, delta))

for delta in deltas:
    print(diff_demo(f, -1, delta))
