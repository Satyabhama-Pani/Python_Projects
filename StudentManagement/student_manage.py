# Student class 
class Student:
    college = "United Institute Of Management"
    def __init__(self,name,roll,marks,classes):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.classes = classes 
    def display(self):
        print("\n"+ "*"*30)
        print(f"{"Student Details":^30}")
        print("*"*30)
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"College: {self.college}")
# School Class
class School:
    students = []
    def menu(self):
        print("\n"+ "*"*40)
        print(f"{"🎓Student Management System":^40}")
        print("*"*40)
        print(f'''
            1. Add Student
            2. View Students
            3. Search Student
            4. Update Marks
            5. Delete Student
            6. View Class Wise Student 
            7. Show Class teacher
            8. Exit
            ''')  
    # Menu Method 
    def menu(self):
        print("\n"+ "*"*40)
        print(f"{"🎓Student Management System":^40}")
        print("*"*40)
        print(f'''
            1. Add Student
            2. View Students
            3. Search Student
            4. Update Marks
            5. Delete Student
            6. View Class Wise Student 
            7. Show Class teacher
            8. Exit
            ''')
    # Add Students
    def add_student(self):
        try:
            self.name = input("Enter a name: ")
            self.roll = int(input("Enter roll number: "))
            self.marks = int(input("Enter marks: "))
            self.classes = int(input("Enter Class of Student: "))
        except ValueError as v:
            print(f"Error : {v}")
            return
        #  If marks is less than 60 student will not be added
        if self.marks >= 60:
            s = Student(self.name,self.roll,self.marks,self.classes)
            self.students.append(s)
            print("\nAdded Succesfully")
        else:
            print("Not qualified in admission test to added")

    #  View Students
    def view_students(self):
        if len(self.students) > 0:
            for student in self.students:
                student.display()
        else:
            print("No records added yet")
            
    #  Search student based on key 
    def search_student(self):
        found = False
        try:
            self.search_roll = int(input("Enter roll number to search the student: "))
        except ValueError as v:
            print(f"Error: {v}")
            return 
        for student in self.students:
            if student.roll == self.search_roll:
                found = True
                print("Student Found")
                student.display()
                break
        if not found:
            print("Student not found") 