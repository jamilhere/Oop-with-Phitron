
class StudentDatabase:
    __student_list = []
    
    @classmethod
    def add_student(cls,student):
        cls.__student_list.append(student)
    
    @classmethod
    def get_all_students(cls):
        return cls.__student_list
    
    @classmethod
    def get_student(cls,student_id):
        for student in cls.__student_list:
            if student.get_student_id() == student_id:
                return student

class Student:
    def __init__(self,student_id,name,department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)
    def get_student_id(self):
        return self.__student_id
    def enroll_student(self):
        if self.__is_enrolled:
            print("Student is already enrolled")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully")
    
    def drop_student(self):
        if not self.__is_enrolled:
            print("Student is already not enrolled")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully")
    
    def view_student(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id}, Name: {self.__name}, Dept: {self.__department}, Status: {status}")

Student("101","jamil","cse")
Student("102","Tuha","Math")
Student("103","jubayer","English")

def menu():
    while True:
        print("\n1. view All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        choice  = input("Enter choice: ")

        if choice == "1":
            for s in StudentDatabase.get_all_students():
                s.view_student()
        
        elif choice == "2":
            sid = input("Enter Student ID to enroll: ")
            student = StudentDatabase.get_student(sid)
            if student:
                student.enroll_student()
            else:
                print("Student not found.")
        
        elif choice == "3":
            sid = input("Enter studnet id to drop: ")
            student = StudentDatabase.get_student(sid)
            if student:
                student.drop_student()
            else:
                print("Student not found")
        elif choice == "4":
            print("Goodbuy")
            break
        
        else:
            print("Invalid choice. Try again.")
        
menu()
