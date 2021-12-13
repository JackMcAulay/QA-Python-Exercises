def get_grade(name, hw_score, as_score, fe_score, percent_grade):
    grade = round(((hw_score + as_score + fe_score) / 175) * 100, 1)

    for i in percent_grade:
        if i[0] <= grade:
            return f"{name} attained the Grade {i[1]}"
    return f"{name} Failed"


score_card = [[95, 'A*'], [80, 'A'], [60, 'B'], [40, 'C'], [30, 'D'], [20, 'E']]

while True:
    student_name = input("Please enter your name :")
    homework = int(input("Please enter your Homework Score :"))
    assess = int(input("Please enter your Assessment Score :"))
    exam = int(input("Please enter your Exam Score :"))

    if homework > 25 or assess > 50 or exam > 100:
        print("You have entered something wrong")
    else:
        break

print(get_grade(student_name, homework, assess, exam, score_card))
