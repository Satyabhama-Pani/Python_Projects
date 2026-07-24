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
        