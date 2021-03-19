# Initialize for all GPAs
overall_count = 0       
overall_points = 0      
overall_gpa = 0   
grade= ""
active = True
grades = {"A+": 4.2, 
"A": 4.0, 
"A-": 3.9,
"B+": 3.7, 
"B": 3.2, 
"B-": 3.0, 
"C+": 2.8, 
"C": 2.2, 
"C-": 2.0, 
"D+": 1.8, 
"D": 1.2, 
"F": 0
}

# Get the first input into variable grade
print("This program takes your entered grades and calculates your GPA for you.")
grade_prompt = "Enter your letter grade for a course: \n"
# def gradeInit():
#     grade = input("Enter your letter grade for a course: \n")
    # grade = user_grade.replace(" ", "")
    # grade = grade.lower()

while active: 
    grade = input(grade_prompt)
    one_points = 0
    one_count = 0
    if grade == "quit":
        active = False
    else:
        if grade in grades:
            while grade != "":
                if grade not in grades:
                    print("Sorry the grade you entered is not valid.")
                elif grade in grades:
                    one_count += 1
                    one_points += grades[grade]
                    grade = input(grade_prompt)
    overall_points += one_points
    overall_count += one_count
overall_gpa = overall_points / overall_count
print("GPA is ", ("%.2f" % overall_gpa))