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