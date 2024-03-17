

# dob_task.py - Task 8 - Practical Task 1

# external files - DOB.txt

# var setup
name = []
bday = []

# loads the DOB.txt file from the dob_task.py location
# only way I could get this to work....
from pathlib import Path

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / 'DOB.txt'

# open the file read only
file = open(TEXT_FILE,'r')

with open(TEXT_FILE,'r') as file :

    # split the line into name and birthday and store in the var's
    for line in file:
        contents = line.split()
        
        # first 2 words in the file - name var
        name.append(contents[:2])
        # anything after the first 2 words - bday var
        bday.append(contents[2:])

# output the lists
print("Name")
for i,name in enumerate(name):
    print("{}".format(" ".join(name)))
    
print("\n\nBirthdate")
for i,bday in enumerate(bday):
    print("{}".format(" ".join(bday)))

#close the file 
file.close()
