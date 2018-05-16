student_arr = []
first_name = []
last_name = []
a1 = []
a2 = []
project = []
test1 = []
test2 = []
a1_grade_scale = 0
a2_grade_scale = 0
project_grade_scale = 0
test1_grade_scale = 0
test2_grade_scale = 0
total_marks = []
grade = []


def option_1():
    fmt = '{:<8}{:20}{:<20}'
    print("Enter A1,A2,PR,T1,T2 : ")

    while True:
        individual_comp = input()
        if individual_comp == "A1":
            print("A1 grades (%.1f)" % a1_grade_scale)
            for i in range(len(student_arr)):
                full_name = first_name[i] + "," + last_name[i]
                print(fmt.format(student_arr[i], full_name, a1[i]))
            break
        elif individual_comp == "A2":
            print("A2 grades (%.1f)" % a2_grade_scale)
            for i in range(len(student_arr)):
                full_name = first_name[i] + "," + last_name[i]
                print(fmt.format(student_arr[i], full_name, a2[i]))
            break
        elif individual_comp == "PR":
            print("Project grades (%.1f)" % project_grade_scale)
            for i in range(len(student_arr)):
                full_name = first_name[i] + "," + last_name[i]
                print(fmt.format(student_arr[i], full_name, project[i]))
            break
        elif individual_comp == "T1":
            print("A1 grades (%.1f)" % test1_grade_scale)
            for i in range(len(student_arr)):
                full_name = first_name[i] + "," + last_name[i]
                print(fmt.format(student_arr[i], full_name, test1[i]))
            break
        elif individual_comp == "T2":
            print("A1 grades (%.1f)" % test2_grade_scale)
            for i in range(len(student_arr)):
                full_name = first_name[i] + "," + last_name[i]
                print(fmt.format(student_arr[i], full_name, test2[i]))
            break
        else:
            print("Wrong input type, please follow the instructions above.")


def option_2():
    print("Enter A1,A2,PR,T1,T2 : ")

    while True:
        individual_comp = input()
        total = 0
        if individual_comp == "A1":
            for x in a1:
                total += x
            total = total/len(a1)
            print("%.1f/%.1f" % (total, a1_grade_scale))
        elif individual_comp == "A2":
            for x in a2:
                total += x
            total = total/len(a2)
            print("%.1f/%.1f" % (total, a2_grade_scale))
        elif individual_comp == "PR":
            for x in project:
                total += x
            total = total/len(project)
            print("%d/%d" % (total, project_grade_scale))
        elif individual_comp == "T1":
            for x in test2:
                total += x
            total = total/len(test1)
            print("%d/%d" % (total, test1_grade_scale))
        elif individual_comp == "T2":
            for x in test2:
                total += x
            total = total/len(test2)
            print("%d/%d" % (total, test2_grade_scale))
        break


def option_3():
    calculate_grades()
    fmt = '{:<8}{:10}{:10}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}'
    print(fmt.format('ID', 'LN', 'FN', 'A1', 'A2', 'PR', 'T1', 'T2', 'GR', 'FL'))
    for i, (id, lnm, fnm, as1, as2, prj, tr1, tr2, gr, fl) in enumerate(
            zip(student_arr, first_name, last_name, a1, a2, project, test1, test2, total_marks, grade)):
        print(fmt.format(id, lnm, fnm, as1, as2, prj, tr1, tr2, gr, fl))


def option_4():
    print("")


def read_files():
    global a1_grade_scale
    global a2_grade_scale
    global project_grade_scale
    global test1_grade_scale
    global test2_grade_scale

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/class.txt") as class_file:
        for line in class_file:
            student_arr.append(line[:5])
            first_name.append(line[line.index('|')+1:line.find('|', 6, len(line))])
            last_name.append(line[line.find('|', 6, len(line))+1:].replace("\n", ""))

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/a1.txt") as a1_file:
        first = True
        for line in a1_file:
            if first:
                a1_grade_scale = float(line)
                first = False
            else:
                a1.append(float(line[6:].replace("\n", "")))

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/a2.txt") as a2_file:
        first = True
        for line in a2_file:
            if first:
                a2_grade_scale = float(line)
                first = False
            else:
                a2.append(float(line[6:].replace("\n", "")))

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/project.txt") as project_file:
        first = True
        for line in project_file:
            if first:
                project_grade_scale = int(line)
                first = False
            else:
                project.append(int(line[6:].replace("\n", "")))

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/test1.txt") as test1_file:
        first = True
        for line in test1_file:
            if first:
                test1_grade_scale = int(line)
                # print("%d" %test1_grade_scale)
                first = False
            else:
                test1.append(int(line[6:].replace("\n", "")))

    with open(r"C:\Users\mahedi\Desktop\COMP-6411/test2.txt") as test2_file:
        first = True
        for line in test2_file:
            if first:
                test2_grade_scale = int(line)
                first = False
            else:
                test2.append(int(line[6:].replace("\n", "")))


def calculate_grades():
    for i in range(len(student_arr)):
        total_tmp = a1[i] + a2[i] + project[i] + test1[i] + test2[i]
        total_marks.append(total_tmp)
        if total_tmp < 50:
            grade.append("F")
        elif total_tmp < 57:
            grade.append("C")
        elif total_tmp < 64:
            grade.append("B-")
        elif total_tmp < 70:
            grade.append("B")
        elif total_tmp < 77:
            grade.append("B+")
        elif total_tmp < 84:
            grade.append("A-")
        elif total_tmp < 90:
            grade.append("A+")


def main():
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
            option_3()
        elif ans == "4":
            print()
        elif ans == "5":
            print()
        elif ans == "6":
            ans = None
            print()
        elif ans != "":  # null input
            print()


read_files()
main()
