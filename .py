import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 2, 4, 5, 6])
y = np.array([5, 7, 9, 7, 11, 13, 14])

# Initialize parameters
m, b = 0, 0
learning_rate = 0.01
iterations = 1000

# Gradient Descent
for _ in range(iterations):
    y_pred = m * X + b #slope of line
    m -= learning_rate * (-2/len(X)) * sum(X * (y - y_pred))
    b -= learning_rate * (-2/len(X)) * sum(y - y_pred)

# Final line equation: y = mX + b
print(f"Slope (m): {m}, Intercept (b): {b}")

# Plot data and regression line
plt.scatter(X, y, color='blue')  # Data points
plt.plot(X, m * X + b, color='red')  # Best fit line
plt.show()
