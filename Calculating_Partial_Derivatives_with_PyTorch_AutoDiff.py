import torch

x = torch.tensor(0.).requires_grad_()
print(x)

y = torch.tensor(0., requires_grad=True)
print(y)


def f(my_x, my_y):
    return my_x**2 - my_y**2


z = f(x, y)  # Forward pass
print(z)

z.backward()  # Autodiff

print(x.grad)

print(y.grad)
