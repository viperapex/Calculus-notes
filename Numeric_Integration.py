# "quadrature" = numerical integration (as opposed to symbolic)
from scipy.integrate import quad


def g(x):
    return x/2


a = quad(g, 1, 2)
print(a)  # first item in the tuple/output is the result,
# the second item is an estimation of the absolute error of the integral, which in this case is essestially zero


def h(x):
    return 2*x


b = quad(h, 3, 4)

print(b)
