import numpy as np
import matplotlib.pyplot as plt

# Load dataset (Courtesy of Gabe's ML Class)
data = np.loadtxt('FA24\WK5\house_prices.txt', delimiter=',')
np.random.shuffle(data)  # Shuffle the data to randomize row order

# Separate features and target after shuffling
square_footage = data[:, 0]  # Feature 1: square footage
num_rooms = data[:, 1]       # Feature 2: number of rooms
prices = data[:, 2]          # Target: price

# Split data into training and validation sets (80/20 split)
split_index = int(0.8 * len(prices))
square_footage_train = square_footage[:split_index]
num_rooms_train = num_rooms[:split_index]
prices_train = prices[:split_index]
square_footage_val = square_footage[split_index:]
num_rooms_val = num_rooms[split_index:]
prices_val = prices[split_index:]

# Calculate mean and standard deviation from training set
footage_mean = np.mean(square_footage_train)
footage_std = np.std(square_footage_train)
rooms_mean = np.mean(num_rooms_train)
rooms_std = np.std(num_rooms_train)

# Normalize using training set statistics
square_footage_train_normalized = (square_footage_train - footage_mean) / footage_std
num_rooms_train_normalized = (num_rooms_train - rooms_mean) / rooms_std
square_footage_val_normalized = (square_footage_val - footage_mean) / footage_std
num_rooms_val_normalized = (num_rooms_val - rooms_mean) / rooms_std

# Hyperparameters
learning_rate = 0.01
num_iterations = 1000

# Initialize weights and bias
bias = 0          # Intercept
weight_1 = 0      # Weight for square footage (slope)
weight_2 = 0      # Weight for number of rooms

cost_history = []

# Gradient Descent on Training Set
for i in range(num_iterations):
    # Prediction on training set
    predictions_train = bias + weight_1 * square_footage_train_normalized + weight_2 * num_rooms_train_normalized
    
    # Cost (Mean Squared Error) on training set
    cost = np.mean((predictions_train - prices_train) ** 2)
    cost_history.append(cost)
    
    # Gradient Calculation
    d_bias = np.mean(predictions_train - prices_train)
    d_weight_1 = np.mean((predictions_train - prices_train) * square_footage_train_normalized)
    d_weight_2 = np.mean((predictions_train - prices_train) * num_rooms_train_normalized)
    
    # Parameter Update
    bias -= learning_rate * d_bias
    weight_1 -= learning_rate * d_weight_1
    weight_2 -= learning_rate * d_weight_2

# Plot cost history to visualize convergence
plt.figure(figsize=(10, 6))
plt.plot(range(num_iterations), cost_history, 'b')
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost Reduction over Iterations")
plt.show()

# Final model parameters
print(f"Bias (intercept): {bias}")
print(f"Weight for square footage: {weight_1}")
print(f"Weight for number of rooms: {weight_2}")

# Make predictions on the validation set
predicted_prices_val = bias + weight_1 * square_footage_val_normalized + weight_2 * num_rooms_val_normalized
validation_cost = np.mean((predicted_prices_val - prices_val) ** 2)
print(f"Validation Cost (Mean Squared Error): {validation_cost}")

# Create a single figure with two subplots for both features in the validation set
plt.figure(figsize=(14, 6))

# Subplot 1: Square Footage vs Price
plt.subplot(1, 2, 1)
plt.scatter(square_footage_val, prices_val, color='blue', label="Actual Prices")
plt.scatter(square_footage_val, predicted_prices_val, color='red', label="Predicted Prices")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.legend()
plt.title("Price Prediction by Square Footage")

# Subplot 2: Number of Rooms vs Price
plt.subplot(1, 2, 2)
plt.scatter(num_rooms_val, prices_val, color='blue', label="Actual Prices")
plt.scatter(num_rooms_val, predicted_prices_val, color='red', label="Predicted Prices")
plt.xlabel("Number of Rooms")
plt.ylabel("Price")
plt.legend()
plt.title("Price Prediction by Number of Rooms")

plt.tight_layout()
plt.show()
