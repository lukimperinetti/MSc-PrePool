# ----- Dictionaries ----- #

import random
import string


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


def task04():
    
    students = [
        {
            'name':'Thomas',
            'academic_year':2023
        },
        {
            'name':'Paul',
            'academic_year':2023
        },
        {
            'name':'Camille',
            'academic_year':2023
        }
    ]
   
    grade_weight_mapping = {
        "A":4,
        "B":3,
        "C":2,
        "D":1,
        "E":0
    }

    for i in students:
        i['unit'] =  [
            {
            'name':'Network and System Administration',
            'credits':random.randint(0,40),
            'grade':chr(random.randint(ord('A'), ord('E')))
            },
            {
            'name':'web development',
            'credits':random.randint(0,40),
            'grade':chr(random.randint(ord('A'), ord('E')))
            },
            {
            'name':'java',
            'credits':random.randint(0,40),
            'grade':chr(random.randint(ord('A'), ord('E')))
            }
        ]

    for index, value in enumerate(students):
        total_credit = 0
    
        gpa_list = []
        for units in value.get('unit'):
            total_credit += units.get('credits') 
            credit = units.get('credits') # me sort les crédits
            grade = units.get('grade') # me sort les grade
            for ele in grade_weight_mapping.keys():
                if grade == ele:
                    gpa_list.append(grade_weight_mapping.get(ele)*credit)
        gpa = sum(gpa_list) / total_credit
        value['GPA'] = round(gpa)
        value['total_credits'] = total_credit #addition des crédit de unit

    # tri par Name
    # sorted_students = sorted(students, key=lambda x: x['name'])
    # print(sorted_students) 

    # tri par GPA
    sorted_students = sorted(students, key=lambda x: x['GPA'])
    print(sorted_students) 
 
   

# task01()
# task02()
# task03()
task04()