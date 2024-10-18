
portfolio = {'AAPL': 50, 'TSLA': 10, 'AMZN': 5}

print("Initial portfolio:", portfolio)

# Access a specific stock directly
#print("Apple shares:", portfolio['AAPL'])

# Use .get() to safely access a stock. Second argument is the value returned if key is not found.
# Returns None by default
#print("Netflix shares:", portfolio.get('NFLX', 'No shares found'))

portfolio['GOOGL'] = 8
portfolio['TSLA'] += 5
#print("Updated portfolio:", portfolio)

# Remove a key value pair with del
del portfolio['AMZN']
#print("After selling Amazon:", portfolio)

# Check if a key is in the dict with "in"
#if 'GOOGL' in portfolio:
#print("Google stock is in the portfolio.")

# Clear the portfolio
portfolio.clear()
#print("Portfolio after selling all stocks:", portfolio)
