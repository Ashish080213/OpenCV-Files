# Creating Custom Generated Data

import matplotlib.pyplot as plt
import random

# y = mx + c
# F = 1.8*C + 32

x = list(range(0, 10)) # Celsius Temperatiure
y = [1.8 * F + 32 for F in x] # Noisy Fahrenheit Temperature
# y = [1.8*F + 32 + random.randint(-3, 3) for F in x] # Noisy Fahrenheit Temperature

print(f'X: {x}')
print(f'Y: {y}')

plt.plot(x, y, '-*r')
plt.show()


