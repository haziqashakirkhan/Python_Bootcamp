print("Welcome to the Age Eligibility Checker!")
age = int(input("Please enter your age: "))

if age < 0 or age > 120:
    print("ERROR: Age cannot be less than 0 or greater than 120")

if age >=18 and age <=60:
    print("You are eligible for  job.")
else:
    print("You are not eligible for job.")