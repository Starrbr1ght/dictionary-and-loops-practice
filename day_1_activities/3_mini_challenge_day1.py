# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

import student_data

def cps_id_exists(cps_id):
    for student in student:
        if student["cps_id"] == cps_id:
            return True
    return False

CPSID= int(input("Enter your CPS ID"))
First_name= input("ejnter your first name")
Last_name= input("enter your last name")
Middle_name= input("enter your middle name")
homeroom= input("enter your homeroom")
grade_level= int(input("enter your grade level"))
Primary_email= input("enter your primary email")
secondary_email= input("enter your second email")


student = {
        "cps_id": CPSID,
        "name": f"{Last_name}, {First_name}",
        "middle_name": Middle_name,
        "homeroom": homeroom,
        "grade_level": grade_level,
        "primary_email": Primary_email,
        "secondary_email": secondary_email
    }

student.update(student)
print("students added")
print("Total students:", len(student))
print(student)

def lookup_student():
    name = input("Enter full name (Last, First): ")

    for student in student:
        if student["name"] == name:
            print("CPS ID:", student["cps_id"])
            print("Homeroom:", student["homeroom"])
            print("Grade Level:", student["grade_level"])
            print("Primary Email:", student["primary_email"])
            return

    print("Student not found.")


# Main loop
while True:
    print("\n1. Lookup Student")
    print("2. Add Student")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        lookup_student()
    elif choice == "2":
        ()
    elif choice == "3":
        break
  # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email