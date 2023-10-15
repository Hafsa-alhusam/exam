class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self):
        print("Enter student details:")
        name = input("Name: ")
        roll_number = input("Roll Number: ")
        age = input("Age: ")
        grade = input("Grade: ")

        student = Student(name, roll_number, age, grade)
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        print("Student List:")
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Student found - Name: {student.name}, Roll Number: {student.roll_number}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found!")

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found!")

    def update_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Updating student with Roll Number: {student.roll_number}")
                student.name = input("New Name: ")
                student.age = input("New Age: ")
                student.grade = input("New Grade: ")
                print("Student updated successfully!")
                return
        print("Student not found!")



def main():
    sms = StudentManagementSystem()

    while True:
        print("\n*** Student Management System Menu ***")
        print("1. Accept Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sms.accept_student()
        elif choice == '2':
            sms.display_students()
        elif choice == '3':
            roll_number = input("Enter Roll Number to search: ")
            sms.search_student(roll_number)
        elif choice == '4':
            roll_number = input("Enter Roll Number to delete: ")
            sms.delete_student(roll_number)
        elif choice == '5':
            roll_number = input("Enter Roll Number to update: ")
            sms.update_student(roll_number)
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")



if __name__ == "__main__":
    main()