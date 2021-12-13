def get_grade(name, hw_score, as_score, fe_score):
    grade = round(((hw_score + as_score + fe_score) / 175) * 100, 1)

    if grade >= 95:
        return f"{name} attained the Grade A*"
    elif grade >= 80:
        return f"{name} attained the Grade A"
    elif grade >= 60:
        return f"{name} attained the Grade B"
    elif grade >= 40:
        return f"{name} attained the Grade C"
    elif grade >= 30:
        return f"{name} attained the Grade D"
    elif grade >= 20:
        return f"{name} attained the Grade E"
    else:
        return f"{name} Failed"


student_name = input("Please enter your name :")
homework = int(input("Please enter your Homework Score :"))
assess = int(input("Please enter your Assessment Score :"))
exam = int(input("Please enter your Exam Score :"))
print(get_grade(student_name, homework, assess, exam))
