scale = input("Which scale do you want to calculate with?\nGlobal(G) scale or AOU(A) scale (G or A)\n=>").upper()

while scale not in ["G","A"]:
    print("Invalid Choice try again!")
    scale = input("Which scale do you want to calculate with?\nGlobal(G) scale or AOU(A) scale (G or A)\n=>").upper()

if scale == "A":
    def get_grade(mark):
        if 90 <= mark <= 100:
            return "A"
        elif 82 <= mark <= 89:
            return "B+"
        elif 74 <= mark <= 81:
            return "B"
        elif 66 <= mark <= 73:
            return "C+"
        elif 58 <= mark <= 65:
            return "C"
        elif 50 <= mark <= 57:
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
        if 90 <= mark <= 100:
            return "A+"
        elif 85 <= mark <= 89.9:
            return "A"
        elif 80 <= mark <= 84.9:
            return "A-"
        elif 75 <= mark <= 79.9:
            return "B+"
        elif 70 <= mark <= 74.9:
            return "B"
        elif 65 <= mark <= 69.9:
            return "B-"
        elif 60 <= mark <= 64.9:
            return "C+"
        elif 55 <= mark <= 59.9:
            return "C"
        elif 50 <= mark <= 54.9:
            return "C-"
        elif 40 <= mark <= 49.9:
            return "D"
        else:
            return "E"

    grades_dict = {
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
    mark = float(input(f"Enter the degree of the {i+1}st course:"))
    while mark < 0 or mark > 100:
        print("Invalid mark, try again")
        mark = float(input(f"Enter the degree of the {i+1}st course:"))
    hours = int(input(f"Enter credit hours of the {i+1}st course:"))
    while hours <= 0:
        print("Invalid hours, try again")
        hours = int(input(f"Enter credit hours of the {i+1}st course:"))
    grade = get_grade(mark)
    points = grade_to_points(grade)

    print(f"{i+1} Course Grade = {grade}, Points = {points}")

    total_hours += hours
    total_points += points * hours

gpa = total_points / total_hours
print(f"GPA: {gpa:.2f}")