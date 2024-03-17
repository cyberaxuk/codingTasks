#while.py - Task4 - Practical Task 1

#ask user for a number
#is the number -1?  - exit and average the numbers
#if the number is not -1 repeat
#output the average of the numbers

#setup vars
number = 0
counter = 0

#loop while number entered is not -1 
while True: 
    new_number_total = int(input("Please enter a number - (-1 will exit)"))

    if new_number_total != -1:
        number += new_number_total
        counter += 1  

    else:    
        break
      
#Output the average of the numbers entered
if counter > 0  :
    print(f"The average of all the numnbers enterered is {number / counter}")

#stops runtime error if the first number is -1
else:
    print("No numbers were entered!")  
