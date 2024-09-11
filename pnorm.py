import numpy as np 
import matplotlib.pyplot as plt

p_values = [0.5, 1, 2, 4, np.inf]
theta = np.linspace(0, 2*np.pi, 1000)

plt.figure(figsize=(8, 8))

for p in p_values:
    if p == np.inf:
        x = np.sign(np.cos(theta))
        y = np.sign(np.sin(theta)) 
    else:
        x = np.cos(theta) 
        y = np.sin(theta) 
        norm = (np.abs(x)**p + np.abs(y)**p) ** (1/p)
        x /= norm
        y /= norm

    plt.plot(x, y, label=f"p = {p}")

plt.title('Visualizing p-Norms')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show() 