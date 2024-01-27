# 1. PRINTING OUTPUT
# Displaying data and results is a fundamental aspect of quantitative analysis.
print("Welcome to FinTech @ IU")

# 2. VARIABLES AND DATA TYPES
# QT deals with a mix of strings, integers, floats, and more.

# Stock ticker as a string:
# QUESTION: What is f at the start of the Print function arguments?
ticker = "AAPL"
print(f"Ticker: {ticker}")

# Stock price as a float:
price = 145.32
print(f"Price: ${price}")

# Trading volume as an integer:
volume = 1000000
print(f"Volume: {volume} shares")

# 3. LISTS AND DATA COLLECTION
# Lists can store historical prices or other financial metrics.
historical_prices = [142.45, 143.5, 144.2, 145.32]
historical_prices_tup = (142.45, 143.5, 144.2, 145.32)

# Representing OHLC for a single day:
ohlc = {
    'open': 143.5,
    'high': 145.0,
    'low': 142.7,
    'close': 144.2
}
print(f"Recent Prices: {historical_prices}")

# 4. CONDITIONAL STATEMENTS
# Conditional logic can be used to make trading decisions.
# We could also send a request to a trading firm given these conditions.
if price > 150:
    print("Consider selling.")
elif price < 140:
    print("Consider buying.")
else:
    print("Hold and monitor.")

# 5. LOOPS
# Loops help in data analysis, especially when dealing with time series data.
for past_price in historical_prices:
    if past_price < 143:
        print(f"Price was below $143 on a day with price: ${past_price}")

# 6. FUNCTIONS
# Functions can encapsulate trading strategies or analysis methods.
def simple_moving_average(prices, days=3):
    """Calculate the Simple Moving Average (SMA) for a given list of prices."""
    return sum(prices[-days:]) / days

sma_value = simple_moving_average(historical_prices)
print(f"3-day SMA: ${sma_value:.2f}")

# 7. IMPORTING MODULES
# Quantitative trading often requires external libraries for complex computations.
# As an introduction, let's use Python's built-in `statistics` for mean and standard deviation.
import statistics

mean_price = statistics.mean(historical_prices)
std_dev_price = statistics.stdev(historical_prices)

print(f"Mean Price: ${mean_price:.2f}")
print(f"Price Standard Deviation: ${std_dev_price:.2f}")

# Self-Guided Practice Problems for Beginner QT

# PROBLEM 1: Simple Profit Calculation
# Given an initial price and a final price, calculate the profit (or loss) for a stock.
initial_price = 140  # Example value, students can change this
final_price = 145    # Example value, students can change this
# TODO: Calculate the profit or loss
# TODO: Print the result with a proper message (e.g., "Profit of $5" or "Loss of $3")

# PROBLEM 2: Extending the Historical Data Analysis
# Given a list of historical prices, calculate the average price and determine the number of days the price was above this average.
historical_prices = [142.45, 143.5, 144.2, 142.9, 145.32, 146, 145.5]  # Example list, students can modify or extend this
# TODO: Calculate the average price
# TODO: Determine the number of days the price was above the average
# TODO: Print the results

# PROBLEM 3: Simple Moving Average (SMA) Calculation
# Using the provided function, calculate and print the 5-day SMA for the `historical_prices` list.
def simple_moving_average(prices, days=3):
    """Calculate the Simple Moving Average (SMA) for a given list of prices."""
    return sum(prices[-days:]) / days
# TODO: Use the above function to calculate the 5-day SMA
# TODO: Print the result

# PROBLEM 4: Conditional Trading Strategy
# Create a basic trading strategy using moving averages. If the current price is greater than the 5-day SMA, suggest selling. Otherwise, suggest buying.
current_price = 145.7  # Example value, students can change this
# TODO: Compare the current price to the 5-day SMA and make a trading suggestion

# PROBLEM 5: Using Statistics for Analysis
# Calculate the median and variance of the `historical_prices` using the `statistics` module. Print the results.
# TODO: Import the necessary functions from the statistics module
# TODO: Calculate the median and variance for `historical_prices`
# TODO: Print the results