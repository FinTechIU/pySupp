ticker = "Apple"
quantity = 23
strike_price = 483.84
total_paid = strike_price * quantity
#stock_info = f"Stock: {ticker}, Quantity: {quantity}, Price bought at: {strike_price}, Total paid: {total_paid}"

#print_info = input("Type Y to print info ")

#if(print_info == "Y"):
#    print(stock_info)
    
#cur_price = input("Type the current price: ")
hit_stop_loss = total_paid <= 460 
hit_price_target = total_paid >= 520
#at_original_price = cur_price == 483.84

should_sell = hit_stop_loss or hit_price_target

"""
if(at_original_price):   
    print("Stock has not moved")
elif(should_sell):
    print("Should sell the stock")
else:
    print("Keep stock at current levels")
"""