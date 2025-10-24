import torch
import matplotlib.pyplot as plt

# E.g. :Dosage of drug for treating Alzheimer's disease
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7])
print(x)

# y = -0.5*x + 2 + torch.normal(mean=torch.zeros), std(0.2)

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


def regression_plot(my_x, my_y, my_m, my_b):

    fig, ax = plt.subplots()

    ax.scatter(my_x, my_y)

    x_min, x_max = ax.get_xlim()
    y_min, y_max = my_m*x_min + my_b, my_m*x_max + my_b

    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])
    plt.show()


regression_plot(x, y, m, b)
