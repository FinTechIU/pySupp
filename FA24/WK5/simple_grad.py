# Define the cost function
def cost_function(x):
    return x ** 2

# Define the derivative (gradient) of the cost function
def gradient(x):
    return 2 * x

# Gradient descent algorithm
def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x  # Start at an initial value of x
    for i in range(num_iterations):
        grad = gradient(x)  # Calculate the gradient at the current x
        x = x - learning_rate * grad  # Move in opposite direction of the gradient
        print(f"Iteration {i+1}: x = {x}, cost = {cost_function(x)}")
    return x

# Parameters
starting_x = 10  # Starting point
learning_rate = 0.1  # Step size
num_iterations = 20  # Number of steps

# Run gradient descent
gradient_descent(starting_x, learning_rate, num_iterations) # 0

