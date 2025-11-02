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


def labeled_regression_plot(my_x, my_y, my_m, my_b, my_C, include_grad=True):
    title = 'Cost = {}'.format('%.3g' % my_C.item())
    if include_grad:
        xlabel = 'm = {}, m grad = {}'.format(
            '%.3g' % my_m.item(), '%.3g' % my_m.grad.item())
        ylabel = 'b = {}, b grad = {}'.format(
            '%.3g' % my_b.item(), '%.3g' % my_m.grad.item())
    else:
        xlabel = 'm = {}'.format('%.3g' % my_m.item())
        ylabel = 'm = {}'.format('%.3g' % my_m.item())

    fig, ax = plt.subplots()

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    ax.scatter(my_x, my_y)

    x_min, x_max = ax.get_xlim()
    y_min = regression(torch.tensor(x_min), my_m, my_b).item()
    y_max = regression(torch.tensor(x_max), my_m, my_b).item()

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max], c='C01')
    plt.show()


labeled_regression_plot(xs, ys, m, b, C)


optimizer = torch.optim.SGD([m, b], lr=0.01)
optimizer.step()

C = mse(regression(xs, m, b), ys)

# Gradient of C hasn't been recalculated
labeled_regression_plot(xs, ys, m, b, C, include_grad=False)
