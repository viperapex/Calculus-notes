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

z = func_z(x, y)
print(z)

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

z = sa_of_cylinder(r, h)
print(z)

z.backward()
print(r.grad)

print(h.grad)

# Task3-> Find all the  partial derivatives of the square prism with a cube cut out of it's centre is described by v=x**2*y-z**3
