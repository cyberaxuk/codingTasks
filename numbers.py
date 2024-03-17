#numbers.py - Task3 - Practical Task 2

#Ask for 3 integers

int1 = int(input("Please enter a number:- "))
int2 = int(input("Please enter a 2nd number:- "))
int3 = int(input("Please enter a 3rd number:- "))

#output the sum of all the numbers
sum_numbers = int1 + int2 + int3
print(f"The numbers total :- ", sum_numbers)

#output 1st number minus 2nd
print(f"The first number minus the second is :- ", int1 - int2)

#output 3rd number * 1st number
print(f"The 3rd number multiplied by the 1st number is :- ", int3 * int1)

#output sum of all 3 numbers / 3rd number
print(f"The sum of all 3 numbers divided by the 3rd number is :-", sum_numbers / int3)