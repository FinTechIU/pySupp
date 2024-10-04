# Strings - Basic features and methods

# Declaring a string
name = "James Demircioglu"
company = "Citadel"
description = "James is the president of Fintech at IU."

#Accessing individual characters
first_char = name[0]
#print("First char of name: " + first_char) #+ sign concatenates (joins) String
last_char = name[-1]
#print("Last char of name: " + last_char)

#Splicing strings
first_name = name[:5] 
#print("First name: " + first_name)
last_name = name[6:]
#print("Last name: " + last_name)

#More methods
length_of_name = len(name)
#print("Length of name: " + length_of_name)
uppercased_name = name.upper()
lowercased_name = name.lower()  
#print("Lowercase: " + lowercased_name)
#print("Uppercase: " + uppercased_name)

formatted_string = f"{name} works at {company} and is the {description[13:33]}."
#print(formatted_string)
