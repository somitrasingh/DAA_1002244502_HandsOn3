# Re-importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import time

# Re-defining f(n) function
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Re-run the zoomed analysis
n_zoom_values_fine = np.arange(1, 100, 10)  # Smaller range for n to zoom in
times_zoom_fine = []

# Measuring times for the smaller range
for n in n_zoom_values_fine:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times_zoom_fine.append(end_time - start_time)

# Using the previous polynomial fit function from quadratic approximation
def poly2(x, a, b, c):
    return a * x**2 + b * x + c

# Example polynomial fit parameters (you may need to refit it)
params = [4.93e-8, -5.83e-6, 5.32e-4]  # From earlier analysis

# Plotting the zoomed-in section to locate n_0
plt.plot(n_zoom_values_fine, times_zoom_fine, label='Measured Time (Zoomed)')
plt.plot(n_zoom_values_fine, poly2(n_zoom_values_fine, *params), '--', label='Quadratic Fit (Zoomed)')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Zoomed-in Time vs n to Find $n_0$')
plt.axvline(x=50, color='r', linestyle='--', label='$n_0$ (approx)')
plt.legend()
plt.grid(True)

plt.show()
