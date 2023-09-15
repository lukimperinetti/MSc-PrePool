# ----- Dictionaries ----- #

def task01():
    students = {'name':'thomas', 'academic_year':2023}
    print(students)


def task02():
    students = {'name':'thomas', 'academic_year':2023}

    students['unit'] =  [
        {
        'name':'Network and System Administration',
        'credits':6,
        'grade':'B'
        },
        {
        'name':'web development',
        'credits':12,
        'grade':'A'
        },
        {
        'name':'java',
        'credits':2,
        'grade':'D'
        }
    ]

    print(students)

def task03():
    students = {'name':'thomas', 'academic_year':2023}

    students['unit'] =  [
        {
        'name':'Network and System Administration',
        'credits':30,
        'grade':'B'
        },
        {
        'name':'web development',
        'credits':35,
        'grade':'A'
        },
        {
        'name':'java',
        'credits':32,
        'grade':'D'
        }
    ]

    grade_weight_mapping = {
        "A":4,
        "B":3,
        "C":2,
        "D":1,
        "E":0
    }

    total_credit = 0
    for credits in students.get('unit'):
        total_credit += credits.get('credits') 

    students['total_credits'] = total_credit #addition des crédit de unit

    gpa_list = []
    for credits in students.get('unit'):
        credit=credits.get('credits') # me sort les crédits
        for ele in grade_weight_mapping.keys():
            if credits.get('grade') == ele:
                gpa_list.append(grade_weight_mapping.get(ele)*credit)
    gpa = sum(gpa_list) / total_credit
    students['GPA'] = round(gpa)
    # print(students)





# task01()
# task02()
task03()