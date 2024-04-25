class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade
        
class Management:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("New Student has been added successfully")

    def display_student_details(self):
        for student in self.students:
            print(f"Student Roll No : {student.roll_no}, Name : {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student Roll No : {student.roll_no}, Name : {student.name}, Age: {student.age}, Grade: {student.grade}")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully")
            else:
                print("Student not found")
    
    def update_student(self, roll_no, name, age, grade):
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = name
                student.age = age
                student.grade = grade 
                print("Student details updated successfully")
                return
        print("Student not in system")

if __name__ == "__main__":
    M = Management()
    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            student = Student(roll_number, name, age, grade)
            M.add_student(student)
        elif choice == '2':
            M.display_student_details()
        elif choice == '3':
            roll_number = input("Enter Roll Number to search: ")
            M.search_student(roll_number)
        elif choice == '4':
            roll_number = input("Enter Roll Number to delete: ")
            M.delete_student(roll_number)
        elif choice == '5':
            roll_number = input("Enter Roll Number to update: ")
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            grade = input("Enter New Grade: ")
            M.update_student(roll_number, name, age, grade)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
      