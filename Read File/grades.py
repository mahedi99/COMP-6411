from operator import attrgetter
from compute import Model, option_1, option_2, option_3, option_4, option_5, calculate_total_marks

a1_grade_scale = 0
a2_grade_scale = 0
project_grade_scale = 0
test1_grade_scale = 0
test2_grade_scale = 0
pass_fail = 50

models = []


def read_files():
    global a1_grade_scale
    global a2_grade_scale
    global project_grade_scale
    global test1_grade_scale
    global test2_grade_scale

    global models

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/class.txt") as class_file:
        for line in class_file:
            model = Model()

            line = line.split('|')
            model.student_id = line[0]
            model.first_name = line[1]
            model.last_name = line[2].replace("\n", "")
            models.append(model)

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/a1.txt") as a1_file:
        first = True
        i = 0
        for line in a1_file:
            if first:
                a1_grade_scale = float(line)
                first = False

            else:
                tmp_a1 = line.split('|')
                models[i].a1 = tmp_a1[1].replace("\n", "")
                i += 1

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/a2.txt") as a2_file:
        first = True
        i = 0
        for line in a2_file:
            if first:
                a2_grade_scale = float(line)
                first = False
            else:
                tmp_a2 = line.split('|')
                models[i].a2 = tmp_a2[1].replace("\n", "")
                i += 1

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/project.txt") as project_file:
        first = True
        i = 0
        for line in project_file:
            if first:
                project_grade_scale = int(line)
                first = False
            else:
                tmp_project = line.split('|')
                models[i].project = tmp_project[1].replace("\n", "")
                i += 1

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/test1.txt") as test1_file:
        first = True
        i = 0
        for line in test1_file:
            if first:
                test1_grade_scale = int(line)
                first = False
            else:
                tmp_t1 = line.split('|')
                models[i].t1 = tmp_t1[1].replace("\n", "")
                i += 1

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/test2.txt") as test2_file:
        first = True
        i = 0
        for line in test2_file:
            if first:
                test2_grade_scale = int(line)
                first = False
            else:
                tmp_t2 = line.split('|')
                models[i].t2 = tmp_t2[1].replace("\n", "")
                i += 1


def main():
    global models

    read_files()
    models = sorted(models, key=attrgetter('student_id'))
    models = calculate_total_marks(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale)

    ans = True
    while ans:
        print("""
        1> Display individual component
        2> Display component average
        3> Display standard report
        4> Sort by alternate column
        5> Change Pass/Fail point
        6> Exit
        """)
        ans = input()
        if ans == "1":
            option_1(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale)
        elif ans == "2":
            option_2(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale)
        elif ans == "3":
            option_3(models, pass_fail)
        elif ans == "4":
            option_4(models, pass_fail)
        elif ans == "5":
            option_5(models, pass_fail)
        elif ans == "6":
            ans = None
            print("Good Bye")
        elif ans != "":  # null input
            print("Wrong input, Input range: 1-6")


main()
