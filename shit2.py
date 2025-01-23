def sum_f(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def average_f(list):
    sum = sum_f(list)
    listlength = len(list)
    average = round(sum/listlength)
    return average

grade_uinput = input('''Give me some grades in the format "1,2,3": ''')
grade_list = list(map(int, grade_uinput.split(",")))
print("Average:", average_f(grade_list))