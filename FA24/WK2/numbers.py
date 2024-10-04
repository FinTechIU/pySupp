# Integers and Floats - Basic features and methods

# Defining integers and floats
age = 22
years_at_company = 3
salary = 1_200_000
bonus_percentage = 0.15
expenses = 53_678.89

# Arithmetic operations
total_income = salary + (salary * bonus_percentage)
#print("Total income: " + str(total_income))

remaining_income = salary - expenses
#print("Remaining income:", remaining_income)

# Integer division and modulus
years_per_position = years_at_company // 2  # Integer division using //
remaining_years = years_at_company % 2  # Modulus gives remainder
#print(f"Years per position: {years_per_position}, Remaining years: {remaining_years}")
#print(f"Had we divided regularly it would be: {years_at_company / 2}") #Regular division will return a float

# Power operation
experience_factor = age ** 2  # age squared (age^2)
#print(f"Experience factor (age squared): {experience_factor}")

# Rounding floats
rounded_expenses = round(expenses, 2)
#print(f"Rounded expenses: {rounded_expenses}")