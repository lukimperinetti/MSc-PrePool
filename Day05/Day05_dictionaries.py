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

    grade_weight_mapping = {
        "A":4,
        "B":3,
        "C":2,
        "D":1,
        "E":0
    }


    


# task01()
# task02()
task03()