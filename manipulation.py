#manipulation.py - Task3 - Practical Task 1

#Ask the user to enter a sentance


str_manip = input("Hey, please enter a sentance :- ")

#Calculate the length on str_manip
print(f"The length of str_manip is", len(str_manip))

#Find the last letter in str_manip and replace every instance with @ and output it
str_manip_last_letter = str_manip[-1:]
print(f"The last letter is {str_manip_last_letter}")

str_manip_replaced = str_manip.replace(str_manip_last_letter, "@")
print(f"All instances of the last letter replaced {str_manip_replaced}")

#Output the last 3 chars of str_manip reversed
str_manip_last_three = str_manip[-3:]
str_manip_last_three = str_manip_last_three[::-1]
print(f"Last 3 chars reversed = {str_manip_last_three}")

#Output 5 letter word = first 3 chars and last 2 of str_manip
print(f"The new word is ", str_manip[0:3] + str_manip[-2::])
