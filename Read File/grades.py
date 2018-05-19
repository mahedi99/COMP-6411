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

    with open('class.txt', 'r') as class_file:
        for line in sorted(class_file):
            model = Model()

            line = line.split('|')
            model.student_id = line[0]
            model.first_name = line[1]
            model.last_name = line[2].replace("\n", "")
            models.append(model)

    with open('a1.txt', 'r') as a1_file:
        a1_grade_scale = float(a1_file.readline())
        i = 0
        for line in sorted(a1_file):
            tmp_a1 = line.split('|')
            models[i].a1 = tmp_a1[1].replace("\n", "")
            i += 1

    with open('a2.txt', 'r') as a2_file:
        a2_grade_scale = float(a2_file.readline())
        i = 0
        for line in sorted(a2_file):
            tmp_a2 = line.split('|')
            models[i].a2 = tmp_a2[1].replace("\n", "")
            i += 1

    with open('project.txt', 'r') as project_file:
        project_grade_scale = int(project_file.readline())
        i = 0
        for line in sorted(project_file):
            tmp_project = line.split('|')
            models[i].project = tmp_project[1].replace("\n", "")
            i += 1

    with open('test1.txt', 'r') as test1_file:
        test1_grade_scale = int(test1_file.readline())
        i = 0
        for line in sorted(test1_file):
            tmp_t1 = line.split('|')
            models[i].t1 = tmp_t1[1].replace("\n", "")
            i += 1

    with open('test2.txt', 'r') as test2_file:
        test2_grade_scale = int(test2_file.readline())
        i = 0
        for line in test2_file:
            tmp_t2 = line.split('|')
            models[i].t2 = tmp_t2[1].replace("\n", "")
            i += 1


def main():
    global models

    read_files()
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
