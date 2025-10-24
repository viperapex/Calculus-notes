import torch

x = torch.tensor(5.0)

print(x)

x.requires_grad_()  # Contagiously track gradients through forward pass

y = x**2

y.backward()  # use autodiff

print(x.grad)
