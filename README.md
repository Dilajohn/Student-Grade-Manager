# Student Grades Manager

## Project Description
The **Student Grades Manager** is a Python-based program designed to manage student grades efficiently using a combination of Python data structures. This tool allows users to add, update, view, and delete student information while maintaining subject-specific grades. Additionally, it supports data persistence through JSON-based saving and loading.

---

## Features

### Core Functionality
1. **Add Student**  
   - Prompts for student ID, name, and subjects.  
   - Uses a `Set` to store unique subjects.  

2. **Add/Update Grades**  
   - Allows adding or updating grades for the student’s subjects.  
   - Uses a `Dictionary` to map subjects to grades.  

3. **View Student**  
   - Displays the student’s ID, name, subjects, and grades.  

4. **Calculate Average Grade**  
   - Calculates and displays the average grade for a specific student.  

### Additional Features
1. **Delete Student**  
   - Allows removing a student by their ID, along with all associated data.  

2. **Save and Load Data**  
   - **Save Data**: Saves student information into a JSON file (`students.json`).  
   - **Load Data**: Automatically loads data from the JSON file when the program starts or initializes an empty system if no file is found.  

---

## Data Structures Used
- **List**: To store and handle grades for each subject.  
- **Tuple**: To store immutable student information (e.g., student ID, name).  
- **Set**: To manage unique subjects for each student.  
- **Dictionary**: To map student names to their grades and manage all student data.  

---

## How to Use
1. **Run the Program**  
   Execute the script in a Python environment.

2. **Main Menu Options**  
   - **1. Add Student**: Enter student ID, name, and subjects.  
   - **2. Add/Update Grades**: Add or update grades for subjects.  
   - **3. View Student**: View detailed information about a specific student.  
   - **4. Calculate Average Grade**: Calculate the average grade for a student.  
   - **5. Delete Student**: Remove a student from the system.  
   - **6. Save Data**: Save all data to `students.json`.  
   - **7. Exit**: Exit the program (automatically saves data).  

---

## Future Extensions
- **Edit Student Details**: Update a student's name or subjects.  
- **Grade Statistics**: Provide additional metrics, such as the highest/lowest grades and subject averages.  
- **Subject-Wise Performance**: Analyze and display performance metrics for each subject.  

---

## Example Commands
To get started:
```bash
python student_grades_manager.py
