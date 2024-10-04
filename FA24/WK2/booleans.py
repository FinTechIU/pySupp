# Booleans - Basic features and methods

is_employed = True
is_graduated = False
has_bonus = True

# Boolean operations (and, or, not)
eligible_for_bonus = is_employed and has_bonus  # True if both conditions are True
#print("Eligible for bonus: " + eligible_for_bonus)

can_start_work = is_graduated or not is_employed  # True if either condition is True
#print("Can start work:", can_start_work) #Comma allows you to concatenate without explicitly converting

# Using booleans in comparisons
age = 22
minimum_working_age = 18
is_of_working_age = age >= minimum_working_age  # True if age is greater than or equal to 18
#print("Is of working age:", is_of_working_age)

# Boolean from numbers
salary = 1_230_534
has_high_salary = salary > 1_000_000  # True if salary is more than 1,000,000
#print("Has high salary:", has_high_salary)

# Boolean from a string
description = "James is the president of Fintech at IU."
contains_president = "president" in description  # True if 'president' is found in the description
#print("Contains 'president':", contains_president)
