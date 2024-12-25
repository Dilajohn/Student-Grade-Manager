#STUDENT GRADE MANAGER -(project)
#Create a program to manage student grades using these data structures.
#Use:
#List: To store grades for each student.
#Tuple: To store immutable student information (ID, name).
#Set: To store unique subjects offered.
#Dictionary: To map student names to their grades.

"""Features of the Program
1-Add Student:
Prompts for student ID, name, and subjects.
Uses a Set to store unique subjects for each student.

2-Add/Update Grades:
Allows adding or updating grades for the student’s subjects.
Uses a Dictionary to map subjects to grades.

3-View Student:
Displays the student’s ID, name, subjects, and grades.

4-Calculate Average Grade:
Calculates and displays the average grade of a student.

Extensions
.Delete a Student: Allow the user to remove a student and their associated data.
.Edit Student Details: Enable updates to a student's name or subjects.
.Save and Load Data: Save the student data to a file and reload it upon restarting the program.
.Grade Statistics: Provide additional metrics like the highest grade, lowest grade, and subject averages.
.Subject-Wise Performance: Analyze and display how students are performing in each subject.

Let’s implement Save and Load Data and Delete a Student. These are practical features that can make the program more robust.

Features Added

>Delete Student:
Users can remove a student by ID, along with all associated data.

>Save and Load Data:
Save Data: Saves the students dictionary to a JSON file (students.json).
Load Data: Reloads the students data when the program starts, or initializes an empty system if no file is found.
"""

import json

def add_student(students):
    """Add a new student."""
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists.")
        return
    name = input("Enter student name: ")
    subjects = input("Enter subjects (comma-separated): ").split(",")
    subjects = set(subject.strip() for subject in subjects)
    students[student_id] = {"name": name, "subjects": subjects, "grades": {}}
    print(f"Student {name} added successfully!")

def add_grade(students):
    """Add or update grades for a student."""
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    
    print(f"Adding grades for {students[student_id]['name']}")
    for subject in students[student_id]["subjects"]:
        grade = float(input(f"Enter grade for {subject}: "))
        students[student_id]["grades"][subject] = grade
    print("Grades updated successfully!")

def view_student(students):
    """View details of a specific student."""
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    
    student = students[student_id]
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Subjects: {', '.join(student['subjects'])}")
    print("Grades:")
    for subject, grade in student["grades"].items():
        print(f"  {subject}: {grade:.2f}")

def calculate_average(students):
    """Calculate and display the average grade for a student."""
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    
    grades = students[student_id]["grades"].values()
    if not grades:
        print("No grades available for this student.")
        return
    
    average = sum(grades) / len(grades)
    print(f"Average grade for {students[student_id]['name']}: {average:.2f}")

def delete_student(students):
    """Delete a student from the system."""
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def save_data(students, filename="students.json"):
    """Save student data to a file."""
    with open(filename, "w") as file:
        json.dump(students, file)
    print("Data saved successfully!")

def load_data(filename="students.json"):
    """Load student data from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved data found. Starting with an empty system.")
        return {}

def main():
    """Main function to manage the program."""
    students = load_data()
    while True:
        print("\nStudent Grades Manager")
        print("1. Add Student")
        print("2. Add/Update Grades")
        print("3. View Student")
        print("4. Calculate Average Grade")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_grade(students)
        elif choice == "3":
            view_student(students)
        elif choice == "4":
            calculate_average(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_data(students)
        elif choice == "7":
            save_data(students)
            print("Thank you for using the Student Grades Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()

