
print("Welcome to the Exam Eligibility Checker!")
    

name = input("Enter your name: ")
age = input("Enter your age: ")
gpa = input("Enter your GPA: ")
attendance = input("Enter your attendance percentage: ")

if int(age) < 18:
        print("Sorry,",name, "you are not eligible because you are below 18 years old.")
   elif float(gpa) < 2.5:
        print("Sorry, " ,name " you are not eligible because your GPA is below 2.5.")
   elif int(attendance) < 75:
        print("Sorry, " ,name ", you are not eligible because your attendance is below 75%.")
   else:
        print("Congratulations, " ,name "! You are eligible for the exam.")


