import torch
import matplotlib.pyplot as plt

# E.g. :Dosage of drug for treating Alzheimer's disease
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7])
print(x)

# patients forgetfulness score
y = torch.tensor([1.86, 1.31, 0.62, 0.33, 0.09, -0.67, -1.23, -1.37])
print(y)

fig, ax = plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (ml)")
plt.ylabel("Forgetfulness")
_ = ax.scatter(x, y)
# plt.show()

m = torch.tensor([0.9]).requires_grad_()
print(m)
b = torch.tensor([0.1]).requires_grad_()
print(b)


def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b


def regression_plot(my_x, my_y, my_m, my_b):
    fig, ax = plt.subplots()
    ax.scatter(my_x, my_y)

    x_min, x_max = ax.get_xlim()

    # Convert tensors to numpy arrays and detach from computation graph
    my_m_np = my_m.detach().numpy()[0]  # Use [0] to get scalar value
    my_b_np = my_b.detach().numpy()[0]  # Use [0] to get scalar value

    y_min = my_m_np * x_min + my_b_np
    y_max = my_m_np * x_max + my_b_np

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])
    plt.show()


regression_plot(x, y, m, b)

"""
 It doesn't yet include:

Loss calculation

Gradient descent optimization

Training loop to update m and b
"""

# Forward Pass

yhat = regression(x, m, b)  # y^ refs newtons notation
print(yhat)


def mse(my_yhat, my_y):
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)


C = mse(yhat, y)

print(C)


# PyTorch Autodiff to calculate gradient of C(Cosst) wrt parameters m and b
C.backward()  # differentiating backwards

print(m.grad)

print(b.grad)

# We pass in the parameters along with learning rate 'lr' to Stochastic gradient descent optimizer function
optimizer = torch.optim.SGD([m, b], lr=0.01)
optimizer.step()

# we see that the parameters are optimized and the cost is lowered
print(m)
print(b)


regression_plot(x, y, m, b)

C = mse(regression(x, m, b), y)
print(C)
