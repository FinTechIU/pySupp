empty_list = []
filled_list = [1, 4.8, "Fintech", True]

#Accesses the first element
print(filled_list[0])
 
#print(filled_list[2])

#Accesses the last element 
#print(filled_list[-1])

#Accesses an out of bounds element
#print(filled_list[4])

#Appends an item at the end
filled_list.append("Element should be at the end of the list")
#print(filled_list[len(filled_list) - 1])

#Adds an element at index 1
filled_list.insert(1, 23.5)
#print(filled_list)

#Removes element at index 1
filled_list.remove(1)
#print(filled_list)

#removes and rerturns an element from the beginning of the list
#print(filled_list.pop())

#Sorts the list
nums_list = [5, 2, 1, 3]
nums_list.sort()
print(nums_list)

#five_day_prices = [23.5, 25.6, 24.8, 24.9, 25]

def calc_five_day_avg(five_day_prices):
    return (five_day_prices[0] + five_day_prices[1] + five_day_prices[2] + five_day_prices[3] + five_day_prices[4]) / len(five_day_prices)
    #return sum(five_day_prices) / len(five_day_prices)

#print(calc_five_day_avg(five_day_prices))