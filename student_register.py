# student_register.py - Task 8 - Practical Task 2

# external files - reg_form.txt

# setup some variables

number_of_students = int(1)
student_id = int(0)
signature_line = "   ............................"
count = int(0)

# open the file write only
file = open('./reg_form.txt', 'w')

# ask for the number of students
number_of_students = int(input("Please enter the number of students :- "))

# write a header to the file to show what its for!
file.write("Exam Register \n\n\n")

# ask for the student id's for the number_of_students
while count < number_of_students :
    student_id = input("Please enter the students id :-")
    # write the input to the file, add additional spaces to leave room for a signature
    file.write(student_id + signature_line + "\n\n\n\n\n")
    count += 1

#close the file 
file.close()