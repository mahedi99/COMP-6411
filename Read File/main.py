from operator import attrgetter
from model import Model

a1_grade_scale = 0
a2_grade_scale = 0
project_grade_scale = 0
test1_grade_scale = 0
test2_grade_scale = 0
pass_fail = 50

models = []


def option_1():
    fmt = '{:<8}{:20}{:<20}'
    print("Enter A1/A2/PR/T1/T2 : ")

    while True:
        individual_comp = input()
        if individual_comp == "A1":
            print("A1 grades (%.1f)" % a1_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].a1))
            break
        elif individual_comp == "A2":
            print("A2 grades (%.1f)" % a2_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].a2))
            break
        elif individual_comp == "PR":
            print("Project grades (%.1f)" % project_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].project))
            break
        elif individual_comp == "T1":
            print("A1 grades (%.1f)" % test1_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].t1))
            break
        elif individual_comp == "T2":
            print("A1 grades (%.1f)" % test2_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].t2))
            break
        else:
            print("Wrong input type, please follow the instructions above.")


def option_2():
    print("Enter A1/A2/PR/T1/T2 : ")

    while True:
        individual_comp = input()
        total = 0
        if individual_comp == "A1":
            for x in models:
                total += x.a1
            total = total/len(models)
            print("%.1f/%.1f" % (total, a1_grade_scale))
        elif individual_comp == "A2":
            for x in models:
                total += x.a2
            total = total/len(models)
            print("%.1f/%.1f" % (total, a2_grade_scale))
        elif individual_comp == "PR":
            for x in models:
                total += x.project
            total = total/len(models)
            print("%d/%d" % (total, project_grade_scale))
        elif individual_comp == "T1":
            for x in models:
                total += x.t1
            total = total/len(models)
            print("%d/%d" % (total, test1_grade_scale))
        elif individual_comp == "T2":
            for x in models:
                total += x.t2
            total = total/len(models)
            print("%d/%d" % (total, test2_grade_scale))
        break


def option_3(model_list):
    fmt = '{:<8}{:10}{:10}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}'
    print(fmt.format('ID', 'LN', 'FN', 'A1', 'A2', 'PR', 'T1', 'T2', 'GR', 'FL'))
    for model in model_list:
        print(fmt.format(model.student_id, model.last_name, model.first_name, model.a1, model.a2, model.project, model.t1, model.t2, model.marks, model.grade))


def option_4():
    print("Sort by LT/GR:")
    while True:
        sort_option = input()
        if sort_option == "LT":
            option_3(sorted(models, key=attrgetter('last_name')))
            break
        elif sort_option == "GR":
            option_3(sorted(models, key=attrgetter('marks'), reverse=True))
            break


def option_5():
    tmp_pass_fail = int(input("Enter Pass/Fail number: "))
    if 0 < tmp_pass_fail < 100:
        calculate_grades(tmp_pass_fail)
        option_3(models)
    calculate_grades(pass_fail)


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


def calculate_grades(tmp_pass_fail):
    mark_range = (100 - tmp_pass_fail)/7
    if mark_range > 0:
        for i in range(len(models)):
            total_tmp = get_calculated_a1(models[i].a1) + get_calculated_a2(models[i].a2) + \
                        get_calculated_project(models[i].project) + get_calculated_test1(models[i].t1) + get_calculated_test2(models[i].t2)
            models[i].marks = total_tmp
            if total_tmp <= tmp_pass_fail:
                models[i].grade = "F"
            elif total_tmp < tmp_pass_fail+(mark_range * 1):
                models[i].grade = "C"
            elif total_tmp < tmp_pass_fail+(mark_range * 2):
                models[i].grade = "B-"
            elif total_tmp < tmp_pass_fail+(mark_range * 3):
                models[i].grade = "B"
            elif total_tmp < tmp_pass_fail+(mark_range * 4):
                models[i].grade = "B+"
            elif total_tmp < tmp_pass_fail+(mark_range * 5):
                models[i].grade = "A-"
            elif total_tmp < tmp_pass_fail+(mark_range * 6):
                models[i].grade = "A-"
            elif total_tmp <= 100:
                models[i].grade = "A+"


def get_calculated_a1(a1):
    if not a1:
        return 0
    else:
        return int(float(a1) / a1_grade_scale * 7.5)


def get_calculated_a2(a2):
    if not a2:
        return 0
    else:
        return int(float(a2) / a2_grade_scale * 7.5)


def get_calculated_project(project):
    if not project:
        return 0
    else:
        return int(float(project)/project_grade_scale * 25)


def get_calculated_test1(t1):
    if not t1:
        return 0
    else:
        return int(float(t1)/test1_grade_scale * 30)


def get_calculated_test2(t2):
    if not t2:
        return 0
    else:
        return int(float(t2)/test1_grade_scale * 30)


def main():

    global models
    models = sorted(models, key=attrgetter('student_id'))

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
            option_1()
        elif ans == "2":
            option_2()
        elif ans == "3":
            option_3(models)
        elif ans == "4":
            option_4()
        elif ans == "5":
            option_5()
        elif ans == "6":
            ans = None
            print("Good Bye")
        elif ans != "":  # null input
            print("Wrong input, Input range: 1-6")


read_files()
calculate_grades(pass_fail)
main()
