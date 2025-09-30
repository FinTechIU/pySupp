import numpy as np

# Create a NumPy array

data = np.array([1, 2, 3, 4, 5])
# Perform operations
print("Array:", data)
mean = np.mean(data)
print("Mean:", mean)
print("Squared:", data ** 2)
print("Mean Squared:", mean ** 2, "Squared Mean:", np.mean(data ** 2))
