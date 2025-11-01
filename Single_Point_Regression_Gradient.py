import torch

xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.])
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])


def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b


m = torch.tensor([0.9]).requires_grad_()
print(m)
b = torch.tensor([0.1]).requires_grad_()
print(m)

i = 7
x = xs[i]
y = ys[i]

print(x)
print(y)


yhat = regression(x, m, b)
print(yhat)


def squared_error(my_yhat, my_y):
    return (my_yhat - my_y)**2


C = squared_error(yhat, y)
print(C)


# Autodiff method
C.backward()

print(m.grad)
print(b.grad)

# Manual method
p = 2*x*(yhat.item()-y)
print(p)
q = 2*(yhat.item()-y)
print(q)


# Gradient calc Pytorch
gradient = torch.tensor([[b.grad.item(), m.grad.item()]]).T
print(gradient)

# All give the same results.
