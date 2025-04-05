import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="Sine Wave", color='b')
plt.plot(x, y2, label="Cosine Wave", color='r')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine and Cosine Waves")
plt.legend()
plt.grid(True)
plt.show()
