# Task1-> Find all the  partial derivatives of the function z = y**3 + 5*x*y

import numpy as np
import torch
import math

# define tensor graph for equation


def func_z(my_x, my_y):
    return my_y**3 + 5*my_x*my_y


# lets take arbitary values for each variable
x = torch.tensor(4.).requires_grad_()
print(x)

y = torch.tensor(2.).requires_grad_()
print(y)

# Forward pass - compute
z = func_z(x, y)
print(z)

# Backward pass to compute all partial derivatives
z.backward()

print(x.grad)
print(y.grad)


# Task2-> Find all the  partial derivatives of the surface area of a cylinder i.e. 2pir**2 +2pi*r*h

# define tensor graph for equation
def sa_of_cylinder(my_r, my_h):
    return 2*math.pi*my_r**2 + 2*math.pi*my_r*my_h


# lets take arbitary values for each variable
r = torch.tensor(2.).requires_grad_()
print(r)

h = torch.tensor(4.).requires_grad_()
print(h)

# Forward pass - compute the surface area
z = sa_of_cylinder(r, h)
print(z)

# Backward pass to compute all partial derivatives
z.backward()
print(r.grad)

print(h.grad)

# Task3-> Find all the  partial derivatives of the square prism with a cube cut out of it's centre is described by v=x**2*y-z**3

# Define the volume function for square prism with cube cut out


def volume(my_x, my_y, my_z):
    return my_x**2 * my_y - my_z**3


# lets take arbitary values for each variable

# Let's take arbitrary values for each variable
x = torch.tensor(3.).requires_grad_()
print(x)
y = torch.tensor(4.).requires_grad_()
print(y)
z = torch.tensor(2.).requires_grad_()
print(z)

# Forward pass - compute the volume
v = volume(x, y, z)
print(f"Volume v: {v}")

# Backward pass to compute all partial derivatives
v.backward()


# Access all partial derivatives
print(f"∂v/∂x: {x.grad}")  # Partial derivative with respect to x
print(f"∂v/∂y: {y.grad}")  # Partial derivative with respect to y
print(f"∂v/∂z: {z.grad}")  # Partial derivative with respect to z
