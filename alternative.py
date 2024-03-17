# alternative.py - Task 7 - Practical Task 1

# go through a supplied string and alternate the string upper and lower case - output it

#function to carry out the conversion
def convert_string(user_string):
    
    # new string declared for the result
    output = ""
    
    # go through the string and convert odd/even postions to upper/lower
    # case until out of chars using enumerate function
    for x, char in enumerate(user_string):
        if x % 2 == 0:
            output += char.upper()
        else:
            output += char.lower()
    return output

# get a string input
user_input = input("Please enter a string to convert :- ")

# make a copy of the string to preserve the original
temp_string = user_input

# call the function to carry out the conversion
output = convert_string(temp_string)

# output
print(f"\nTa da! :- {output}")

# 2nd part re-submitted as I missed it out....

# split the original user input into a new var
user_input_split = user_input.split()

# alternive words upper/lower capitals
convert_words = " ".join([x.upper() if i % 2 else x.lower() for i, x in enumerate(user_input_split)])

# output the result
print(f"\nAlternate words converted is :- {convert_words}")