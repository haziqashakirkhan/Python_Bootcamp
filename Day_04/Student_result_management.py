print("================================")
print("STUDENT RESULT MANAGEMENT SYSTEM")
print("================================")

student = "haziqa"
marks = 85

while True:
    print("Please select an option:")
    print("1. view student details")
    print("2. update marks")
    print("3. check grade")
    print("4. exit")
    option = int(input("\nPlease select an option: "))

    if option == 1:
        print("student_name =", student)
        print("marks:", marks)

    elif option == 2:
        new_marks = int(input("Enter new marks: "))
        if new_marks < 0 or new_marks > 100:
            print("Invalid marks. Please enter a valid number between 0 and 100.")
            continue
        marks = new_marks
        print("Marks updated successfully.")

    elif option == 3:
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        print("Grade:", grade)

    elif option == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")