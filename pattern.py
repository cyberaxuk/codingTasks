#pattern.py - Task4 - Practical Task 2

#output astericks up to 5 and back down again

# How many rows?
total_rows = 5

# loop until done
for row in range(1, total_rows * 2):
    # Work out the asterisks for current row until total_row = 5
    if row <= total_rows:
        asterisks = row   
    
    else:
       asterisks = 2 * total_rows - row
     
    # Output asterisks
    print("*" * asterisks)

#took a long time and some extra reading to get here....