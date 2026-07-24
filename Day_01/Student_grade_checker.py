print("welcome to the Student Grade Checker!")

name = str(input("Please enter the student's name: "))
marks = int(input("Please enter the student's marks (out of 100): "))

print("===============================")
print("         Result                 ")
print("===============================")

if marks >=90:
    if marks > 100:
     print("ERROR: Marks cannot be greater than 100")
    else:
      print("name:",name)
      print("marks:",marks)
      print("grade: A+")
elif marks >= 80:
    print("name:",name)
    print("marks:",marks)
    print("grade: A")
elif marks >= 70:
    print("name:",name)
    print("marks:",marks)
    print("grade: B")
elif marks >= 60:
    print("name:",name)
    print("marks:",marks)
    print("grade: C")
else:
    print("name:",name)
    print("marks:",marks)
    print("grade: F")
    print("need improvement")
    
print ("Best Regards......")
    

