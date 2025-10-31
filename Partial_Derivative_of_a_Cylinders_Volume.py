import numpy as np
import matplotlib.pyplot as plt
import torch
import math  # for constant pi


def cylinder_vol(my_r, my_l):
    return math.pi * my_r**2 * my_l


# Lets say rhe radius ois 3 meters..
r = torch.tensor(3.).requires_grad_()
print(r)

# ..and length is 5 meters.
l = torch.tensor(5., requires_grad=True)
print(l)

# Then the volume of the cylinder is 121.4 cubic meters:
v = cylinder_vol(r, l)
print(v)

v.backward()  # del v

# /del l ---shows the gradient val or partial derivative when l is kept constant.
print(l.grad)

print(math.pi * 3**2)  # same value when done manually
# This means that with r=3, a change in l by one unit corresponds to a change in v of 28.27m**3.

# lets prove this by different inputs

a = cylinder_vol(3, 6)
print(a)

print(a-v)
