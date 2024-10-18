import random


def average_prices_for(prices):
    sum = 0
    for price in prices:
        sum +=  price
    return sum / len(prices)

def average_prices_while(prices):
    sum = 0
    index = 0
    while index != len(prices):
        sum += prices[index]
        index += 1
    return sum / len(prices)

prices = [25.5, 34, 33, 24, 54]

#print(f"Average price with for method: {average_prices_for(prices)}")
#print(f"Average price with while method: {average_prices_while(prices)}")

def guess_a_number():
    random_number = random.randint(1, 10)
    while(True):
        guess = input("Type your guess of a number 1-10: ")
        if int(guess) == random_number:
            print("Right guess, goodbye!")
            break
        print("Wrong guess, try again")
        
#guess_a_number()

def print_times_tables(start, end):
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            print(f"{i} * {j} = {i * j}")

#print_times_tables(1, 10)
