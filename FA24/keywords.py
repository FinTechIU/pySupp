'''

False, await, else, import, pass, None, break, except, in, raise, True, class, finally, is, return, and, continue, for, lambda, try, as, def, from, nonlocal, while, assert, del, global, not, with, async, elif, if, or, yield

'''

'''

Not demo'd yet:

None, except, raise, class, finally, is, try, assert, del, yield

'''

# False and True are the two boolean values
print('False, True:')

if True:
    print('This will be printed!')
if False:
    print('This will not be printed.')

# not, or, and are boolean operators
print('\nor:')

print(True or False) # prints True
print(True or True) # prints True
print(False or False) # prints False

print('\nand:')

print(True and True) # prints True
print(True and False) # prints False
print(False and True) # prints False
print(False and False) # prints False

print('\nnot:')

print(not True) # False
print(not False) # True

# def, return, and lambda all deal with functions
print('\ndef, return:')

# A function has zero or more arguments, seperated by commas
def function_name(argument1, argument2):
	return_value = argument1 * argument2 # More code can go here
	return return_value

print(function_name(17.5, 4)) # prints 70.0
	
# Lambda define anonymous functions
print('\nlambda:')

def apply_lambda(fxn, arg1, arg2):
	return fxn(arg1, arg2)
	
print(apply_lambda(lambda x,y: x + y, 2, 3)) # prints 5 [2 + 3]

# global allows you to modify global variables within a function
print('\nglobal:')

some_global_variable = "Global"

def global_example_function():
	global some_global_variable
	some_global_variable = "Modified by global_example_function()"

print(some_global_variable) # Prints 'Global'
global_example_function()
print(some_global_variable) # Prints 'Modified by global_example_function()'

# nonlocal is like global, but for functions within other functions
print('\nnonlocal:')

def nonlocal_outer_function():
	some_variable = 'outer'
	print(some_variable) # Prints 'outer'
	def nonlocal_inner_function():
		nonlocal some_variable
		some_variable = 'inner'
		return
	
	nonlocal_inner_function() # Calling this inner function will overwrite some_variable
	print(some_variable) # Prints 'inner'

nonlocal_outer_function()

'''
Note: Since global and nonlocal allow functions to modify state (also known as having side effects),
nonlocal and global should be used sparingly

'''

# if, elif, else let you perform conditional operations
print('\nif:')

if_num = 1 # You can change this value

if if_num == 1:
	print('if_num is 1')
elif if_num == 2:
	print('if_num is 2')
else:
	print('if_num is neither 1 or 2')

# while, for allow you to perform repeated operations in a loop
print('\nwhile:')

loop_variable = 1
last_number = 10
condition = True

while condition: # This condition could be replaced by 'while loop_variable <= last_number:'
	print(loop_variable, end=' ')
	loop_variable = loop_variable + 1
	if loop_variable > last_number:
		condition = False
print() # Prints '1 2 3 4 5 6 7 8 9 10'

start_range = 1 # Feel free to change these and see what happens
end_range = 10 
range_step = 1

print('\nfor:')

for i in range(start_range, end_range + 1, range_step):
	print(i, end=' ')
print() # Also prints '1 2 3 4 5 6 7 8 9 10'

# break and continue allow you to prematurely end a loop or skip to the next iteration
print('\nbreak:')

while True:
	print('This will only print once.')
	break # Normally the True condition will keep this while loop running, but break tells Python to exit it prematurely

for i in range(0, 1 + 1):
	print(i, end=' ') # Prints 0, then 1 on the second iteration
	continue
	print('This will not be printed because of the continue statement above it.')
print()

# in checks whether a value is in a set
print('\nin:')

def print_in(value, set_or_list):
	print(value, end='')
	if value in set_or_list:
		print(' is ', end='')	
	else:
		print(' is not ', end='')
	print('in ' + str(set_or_list))
	return
	
print_in(1, range(2, 10)) # Will print '1 is not in range(2, 10)'
print_in(1, [1, 2]) # Will print '1 is in [1, 2]'
print_in('string', {'set', 'of', 'string', 's'}) # Will print 'string is in { [some arrangement of the members of the defined set] }'
# If you try running this several times, you will notice the set is in different orders each time.
# This is because sets have no concept of order.

# import, as, and from all deal with using Python libraries
print('\nimport:')

import random # Imports the built-in Python random number library

print(random.random()) # Prints a random decimal between 0 and 1

# as allows you to abbreviate imports
print('\nas:')

import random as rd
print (rd.randint(1, 10)) # Prints a random integer (whole number) between 1 and 10 (inclusive).

# from allows you to import specific parts of a library, and can be combined with as.
print('\nfrom:')

from random import random as r
print(r()) # Does the same thing as random.random(), but without having to use the full library and function name

# pass does nothing. It is useful because functions and if, elif, and else blocks need at least one line
print('\npass:')

def do_nothing():
	pass # Pass stops the Python interpreter from throwing an error when a otherwise empty code block is created

do_nothing()

'''
def do_nothing:
print('whatever')

This would normally result in an error, so pass is needed to prevent an error.
You can try removing the pass from the above code, and see what happens.
'''

'''
There a are few more keywords not documented above:

with is used to manage contexts and is commonly used when working with files
We'll come back to this when we talk about file I/O.

async and await allow for asynchronous code
Useful for web operations, but not worth focusing on for beginners.

'''