
print("Welcome to the Exam Eligibility Checker!")
    

name = input("Enter your name: ")
age = input("Enter your age: ")
gpa = input("Enter your GPA: ")
attendance = input("Enter your attendance percentage: ")

if int(age) < 18:
    print("sorry, you are not elidgeble for this exam because you are under 18")
elif float(gpa) < 2.5:
    print("Sorry, you are not elidgeble for this exam because your GPA is too low")
elif int(attendance) < 70:
    print("Sorry, you are not elidgeble for this exam because your attendance is too low")


