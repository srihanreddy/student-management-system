class Student:
    def __init__(self,student_id,student_name,CGPA,age,branch):
        self.Student_name=student_name
        self.Student_id=student_id
        self.CGPA=CGPA
        self.age=age
        self.Branch=branch
    def add_student(self):
        self.Student_id=input("Enter the student id:")
        self.Student_name=input("Enter the student name:")
        self.CGPA=float(input("Enter the student CGPA:"))
        self.age=int(input("Enter the student age:"))
        self.Branch=input("Enter the student branch:")
        student1=Student(self.Student_id,self.Student_name,self.CGPA,self.age,self.Branch)
        return student1
    def display_student(self,student1):
        print("Student_ID:",student1.Student_id)
        print("Student_name:",student1.Student_name)
        print("CGPA:",student1.CGPA)
        print("Age:",student1.age)
        print("Branch:",student1.Branch)
def search_student(students, student_id):
    for student in students:
        if student.Student_id == student_id:
            return student
    return None
def delete_student(students,Student_id):
    for index, student in enumerate(students):
        if student.Student_id==Student_id:
            del students[index]
            return True
    return False
def update_student(students,Student_id,choice):
    for student in students:
        if student.Student_id==Student_id:
            while True:
                if(choice.lower()=="name"):
                    student.Student_name=input("Enter the new name:")
                elif(choice.lower()=="cgpa"):
                    student.CGPA=float(input("Enter the new CGPA:"))
                elif(choice.lower()=="age"):
                    student.age=int(input("Enter the new age:"))
                elif(choice.lower()=="branch"):
                    student.Branch=input("Enter the new branch:")
                else:
                    print("Invalid choice.")
                choice=input("Do you want to update anything else? (yes/no): ")
                if choice.lower()!="yes":
                    break
            return True
    return False
                

s = Student("", "", 0.0, 0, "")
students=[]
student1 = s.add_student()
students.append(student1)
print("\n===========STUDENT MANAGEMENT SYSTEM===========")
print("1.Add Student")
print("2.Display Student")
print("3.Search Student")
print("4.Delete Student")
print("5.Update Student")
print("6.Exit")
choice = input("enter your choice:")
if(choice=="1"):
    student1 = s.add_student()
    students.append(student1)
elif(choice=="2"):
    for student in students:
        s.display_student(student)
elif(choice=="3"):
    student_id = input("Enter the student ID to search: ")
    found_student = search_student(students, student_id)
    if found_student:
        print("Student found:")
        s.display_student(found_student)
    else:
        print("Student not found.")
elif(choice=="4"):
    student_id = input("Enter the student ID to delete: ")
    if delete_student(students, student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")
elif(choice=="5"):
    student_id = input("Enter the student ID to update: ")
    choice = input("Enter field to update (name/cgpa/age/branch): ")
    if update_student(students, student_id, choice):
        print("Student updated successfully.")
    else:
        print("Student not found.")