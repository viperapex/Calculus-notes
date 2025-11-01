import torch
import matplotlib.pyplot as plt

xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])


def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b


m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()

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

# autodiff to calculate gradient C wrt parameters m and b
C.backward()

print(m.grad)
print(b.grad)
