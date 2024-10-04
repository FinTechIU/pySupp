#Function examples

# Function to calculate the total value of stocks
def calculate_total_value(quantity, price_per_stock):
    total_value = quantity * price_per_stock
    return total_value

# Function to calculate profit or loss
def calculate_profit_or_loss(buy_price, sell_price, quantity):
    total_buy = buy_price * quantity
    total_sell = sell_price * quantity
    profit_or_loss = total_sell - total_buy
    return profit_or_loss

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest

# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

# Function to calculate total value of stocks from user input
def calculate_total_value_from_input():
    quantity = int(input("Enter the number of stocks you own: "))
    price_per_stock = float(input("Enter the price of one stock: "))
    total_value = quantity * price_per_stock
    return total_value

# Example usage of the functions
quantity = 10
price_per_stock = 150
total_value = calculate_total_value(quantity, price_per_stock)
print(f"Total value of stocks: ${total_value}")

buy_price = 100
sell_price = 120
quantity = 10
profit_or_loss = calculate_profit_or_loss(buy_price, sell_price, quantity)
print(f"Profit or Loss: ${profit_or_loss}")

principal = 1000
rate = 0.05
time = 3
interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: ${interest}")

principal = 1000
rate = 0.05
time = 3
n = 4
amount = calculate_compound_interest(principal, rate, time, n)
print(f"Final amount after compound interest: ${amount:.2f}")

total_value = calculate_total_value_from_input()
print(f"Total value of stocks: ${total_value}")