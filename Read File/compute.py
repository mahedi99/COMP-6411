from operator import attrgetter


class Model:
    student_id = ""
    first_name = ""
    last_name = ""
    a1 = ""
    a2 = ""
    project = ""
    t1 = ""
    t2 = ""
    marks = ""
    grade = ""


def option_1(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale):
    fmt = '{:<8}{:20}{:<20}'
    print("Enter A1/A2/PR/T1/T2 : ")

    while True:
        individual_comp = input()
        if individual_comp.upper() == "A1":
            print("A1 grades (%d)" % a1_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].a1))
            break
        elif individual_comp.upper() == "A2":
            print("A2 grades (%d)" % a2_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].a2))
            break
        elif individual_comp.upper() == "PR":
            print("Project grades (%d)" % project_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].project))
            break
        elif individual_comp.upper() == "T1":
            print("A1 grades (%d)" % test1_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].t1))
            break
        elif individual_comp.upper() == "T2":
            print("A1 grades (%d)" % test2_grade_scale)
            for i in range(len(models)):
                full_name = models[i].first_name + "," + models[i].last_name
                print(fmt.format(models[i].student_id, full_name, models[i].t2))
            break
        else:
            print("Wrong input type, please follow the instructions above.")


def option_2(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale):
    print("Enter A1/A2/PR/T1/T2 : ")

    while True:
        individual_comp = input()
        total = 0
        if individual_comp.upper() == "A1":
            for x in models:
                if not x.a1:
                    total += 0
                else:\
                    total += int(x.a1)
            total = total/len(models)
            print("%.1f/%d" % (total, a1_grade_scale))
        elif individual_comp.upper() == "A2":
            for x in models:
                if not x.a2:
                    total += 0
                else:
                    total += int(x.a2)
            total = total/len(models)
            print("%.1f/%d" % (total, a2_grade_scale))
        elif individual_comp.upper() == "PR":
            for x in models:
                if not x.project:
                    total += 0
                else:
                    total += int(x.project)
            total = total/len(models)
            print("%.1f/%d" % (total, project_grade_scale))
        elif individual_comp.upper() == "T1":
            for x in models:
                if not x.t1:
                    total += 0
                else:
                    total += int(x.t1)
            total = total/len(models)
            print("%.1f/%d" % (total, test1_grade_scale))
        elif individual_comp.upper() == "T2":
            for x in models:
                if not x.t2:
                    total += 0
                else:
                    total += int(x.t2)
            total = total/len(models)
            print("%.1f/%d" % (total, test2_grade_scale))
        break


def option_3(models, pass_fail):

    models = calculate_grades(models, pass_fail)
    fmt = '{:<8}{:10}{:10}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}'
    print(fmt.format('ID', 'LN', 'FN', 'A1', 'A2', 'PR', 'T1', 'T2', 'GR', 'FL'))
    for model in models:
        print(fmt.format(model.student_id, model.last_name, model.first_name, model.a1, model.a2, model.project, model.t1, model.t2, model.marks, model.grade))


def option_4(models, pass_fail):
    print("Sort by LT/GR:")
    while True:
        sort_option = input()
        if sort_option.upper() == "LT":
            option_3(sorted(models, key=attrgetter('last_name')), pass_fail)
            break
        elif sort_option.upper() == "GR":
            option_3(sorted(models, key=attrgetter('marks'), reverse=True), pass_fail)
            break
        else:
            print("Wrong input!")


def option_5(models, pass_fail):
    tmp_pass_fail = int(input("Enter Pass/Fail number: "))
    calculate_grades(models, tmp_pass_fail)
    if 0 < tmp_pass_fail < 100:
        option_3(models, tmp_pass_fail)
    calculate_grades(models, pass_fail)


def calculate_total_marks(models, a1_grade_scale, a2_grade_scale, project_grade_scale, test1_grade_scale, test2_grade_scale):
    for i in range(len(models)):
        total_tmp = get_calculated_a1(models[i].a1, a1_grade_scale) + get_calculated_a2(models[i].a2, a2_grade_scale) + \
                get_calculated_project(models[i].project, project_grade_scale) + get_calculated_test1(models[i].t1, test1_grade_scale) + get_calculated_test2(models[i].t2, test2_grade_scale)
        models[i].marks = total_tmp

    return models


def calculate_grades(models, tmp_pass_fail):
    mark_range = (100 - tmp_pass_fail)/7
    if mark_range > 0:
        for i in range(len(models)):
            total_tmp = models[i].marks
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
    return models


def get_calculated_a1(a1, a1_grade_scale):
    if not a1:
        return 0
    else:
        return int(float(a1) / a1_grade_scale * 7.5)


def get_calculated_a2(a2, a2_grade_scale):
    if not a2:
        return 0
    else:
        return int(float(a2) / a2_grade_scale * 7.5)


def get_calculated_project(project, project_grade_scale):
    if not project:
        return 0
    else:
        return int(float(project)/project_grade_scale * 25)


def get_calculated_test1(t1, test1_grade_scale):
    if not t1:
        return 0
    else:
        return int(float(t1)/test1_grade_scale * 30)


def get_calculated_test2(t2, test2_grade_scale):
    if not t2:
        return 0
    else:
        return int(float(t2)/test2_grade_scale * 30)