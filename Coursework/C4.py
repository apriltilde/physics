import random
import numpy as np
import matplotlib.pyplot as plt
import math 

#%% 1
z = np.random.normal(0,2,5000)
zbar = np.mean(z)
zsigma = np.std(z)
print("mean = " , round(zbar,3), "\nstandard deviation = " , round(zsigma,3))

x = np.linspace(-9, 9, num=37)
x1 = np.linspace(-9, 9, num=181)
y1 = np.linspace(-9, 9, num=181)
for i in  range(181):
    y1[i] = (5000 / (zsigma * math.sqrt(2 * math.pi))) * math.exp(-(x1[i]**2) / (2 * zsigma**2)) * 0.1


plt.hist(z, x, rwidth = 0.7)
plt.show()

plt.figure()
plt.plot(x1, y1, color="red")
plt.hist(z, x1, rwidth = 0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian")
plt.show()



#%% 2
y = z[:500]
y2 = np.linspace(-9, 9, num=181)
for i in  range(181):
    y2[i] = (500 / (zsigma * math.sqrt(2 * math.pi))) * math.exp(-(x1[i]**2) / (2 * zsigma**2)) * 0.1

plt.figure()
plt.plot(x1, y2, color="red")
plt.hist(y, x1)
plt.show()
