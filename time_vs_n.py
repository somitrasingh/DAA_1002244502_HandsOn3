# Question 2
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to measure
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Timing the function for various values of n
n_values = np.arange(1, 2000, 10)  # Test values of n from 1 to 500
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the time vs n values
plt.plot(n_values, times, label='Measured Time')

# Fitting a quadratic curve to the data
def poly2(x, a, b, c):
    return a * x**2 + b * x + c

params, _ = curve_fit(poly2, n_values, times)
fitted_curve = poly2(n_values, *params)

# Plot the fitted curve
plt.plot(n_values, fitted_curve, '--', label='Quadratic Fit')

# Labels and legend
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time vs n for Function f(n)')
plt.legend()
plt.grid(True)
plt.savefig('time_VS_n.png')
plt.show()

