import numpy as np
import matplotlib.pyplot as plt
import torch
import math  # for constant pi

# define tensor graph


def cylinder_vol(my_r, my_l):
    return math.pi * my_r**2 * my_l


# Lets say the radius is 3 meters..
r = torch.tensor(3.).requires_grad_()
print(r)

# ..and length is 5 meters.
l = torch.tensor(5.).requires_grad_()
print(l)

# Then the volume of the cylinder is 121.4 cubic meters:
v = cylinder_vol(r, l)
print(v)

v.backward()  # del v
# /del l ---shows the gradient val or partial derivative of wrt  l when l is kept constant.
print(l.grad)


print(math.pi * 3**2)  # same value when done manually
# This means that with r=3, a change in l by one unit corresponds to a change in v of 28.27m**3.

# lets prove this by different input instead of l=5 we take l=6

# difference bw a and v is 28.3 which proves the above
cylinder_vol(3, 6) - cylinder_vol(3, 5)


# v.backward # del v
# /del r ---shows the gradient val or partial derivative for r when 2pi and l are kept constant.
print(r.grad)


print(2 * math.pi * 3 * 5)  # same value when done manually

"""
r is includeed in the partial derivative do adjusting it affects the scale
of its impacton v. ALthough it's our first example in this notebook, 
it is typical in calculus for the derivative only to apply at an infinitesimally small 'delta r'.
The smaller the 'delta r', the closer to the true 'pdel v/ pdel r.
"""

delta = 1e-6

# Dividing by delta restores scale
print((cylinder_vol(3 + delta, 5) - cylinder_vol(3, 5)) / delta)
