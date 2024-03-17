#award.py - Task3 - Practical Task 3

#Ask for times for each event
swim_time = float(input ("Enter swim time :- "))
cycle_time = float(input ("Enter cycle time :- "))
run_time = float(input ("Enter run time :- "))

#calculate total time and display it
total_time = swim_time + cycle_time + run_time
print(f"The total time is :-", total_time)

#determine award based on time and output it
if total_time <= 100 : 
    award = "Provincial Colours"
elif total_time <= 105 : 
    award = "Provincial Half Colours"
elif total_time <= 110 : 
    award = "Provincial Scroll"
else : award = "No Award"
print(f"Your award is :-", award)
