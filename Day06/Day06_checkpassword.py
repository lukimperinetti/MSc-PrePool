def func1(string, number):
        print("Function 1")
        count=0
        for i in string:
            if i.islower():
                count += 1
                if count >= number:
                    return True
        return False

def check_password(rule, number, password):
    if rule == 'lower':
        return func1(password, number)