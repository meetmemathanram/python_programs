from __builtin__ import str
salary = int(input('Enter the salary. '))
employer_type = str(raw_input('Enter the type of employer. '))

def showpt(salary , employer_type):
    if(employer_type == "government"):
      print(salary)
    else:
        tax = 0.25*salary
        print(tax+salary)

showpt(salary, employer_type)     