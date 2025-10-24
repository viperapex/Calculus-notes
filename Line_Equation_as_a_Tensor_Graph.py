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
plt.show()
