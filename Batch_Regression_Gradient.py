import torch
import matplotlib.pyplot as plt

xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])


def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b


m = torch.tensor([0.9]).requires_grad_()
print(m)
b = torch.tensor([0.1]).requires_grad_()
print(m)

# Forward pass
yhats = regression(xs, m, b)
print(yhats)

# define mean squared error


def mse(my_yhat, my_y):
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)


# Compare yhat with true y to calculate cost
C = mse(yhats, ys)
print(C)

# using autodiff to calculate gradient C wrt parameters m and b
C.backward()

# param m
print(m.grad)
# param b
print(b.grad)


# using manual derivation

# param
g = 2*1/len(ys)*torch.sum((yhats - ys)*xs)
print(g)

# param b
print(2*1/len(ys)*torch.sum(yhats - ys))


gradient = torch.tensor([[b.grad.item(), m.grad.item()]]).T
print(gradient)
