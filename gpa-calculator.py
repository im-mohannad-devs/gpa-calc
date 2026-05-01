
print("========================================================================\n\t\t\tGPA Calculator\n========================================================================")

scale = input("Which scale do you want to calculate with?\nGlobal(G) scale or AOU(A) scale (G or A)\n=>").upper()
print("========================================================================")
while scale not in ["G","A"]:
    print("Invalid Choice try again!")
    scale = input("Which scale do you want to calculate with?\nGlobal(G) scale or AOU(A) scale (G or A)\n=>").upper()

if scale == "A":
    def get_grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 82:
            return "B+"
        elif mark >= 74:
            return "B"
        elif mark >= 66:
            return "C+"
        elif mark >= 58:
            return "C"
        elif mark >= 50:
            return "D"
        else:
            return "Fail"
    grades_dict = {
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D": 1.5,
        "Fail": 0
    }

elif scale == "G":
    def get_grade(mark):
        if mark >= 90:
            return "A+"
        elif mark >= 85:
            return "A"
        elif mark >= 80:
            return "A-"
        elif mark >= 75:
            return "B+"
        elif mark >= 70:
            return "B"
        elif mark >= 65:
            return "B-"
        elif mark >= 60:
            return "C+"
        elif mark >= 55:
            return "C"
        elif mark >= 50:
            return "C-"
        elif mark >= 40:
            return "D"
        else:
            return "E"
    grades_dict= {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D": 1.0,
        "E": 0.0,
    }

def grade_to_points(grade):
    return grades_dict[grade]

num = int(input("Type Number of courses:"))
while num <= 0:
    print("Invalid number, try again")
    num = int(input("Type Number of courses:"))

total_hours = 0
total_points = 0

for i in range(num):
    mark = float(input(f"Enter the degree of course {i+1}:"))
    while mark < 0 or mark > 100:
        print("Invalid mark, try again")
        mark = float(input(f"Enter the degree of course {i+1}:"))
    hours = int(input(f"Enter credit hours of course {i+1}:"))
    while hours <= 0:
        print("Invalid hours, try again")
        hours = int(input(f"Enter credit hours of course {i+1}:"))
    grade = get_grade(mark)
    points = grade_to_points(grade)

    print(f"Course {i+1} Grade = {grade}, Points = {points}")

    total_hours += hours
    total_points += points * hours

gpa = total_points / total_hours
print(f"GPA: {gpa:.2f}")
