#!/usr/bin/python3

def make_employer(fname, sname, prof):
    if prof == 'programmer':
        sal = 3000
    elif prof == 'driver':
        sal = 1000
    else:
        sal = 0 
    
    return {'first_name': fname,
            'second_name' : sname,
            'profession' : prof,
            'salary' : sal,}

def set_salary(empl, salary):
    empl['salary'] = salary

def update_employers_salary(employers, k):
    for empl in employers:
        empl['salary']  = empl['salary'] * k



employers = []

employers.append(make_employer('John', 'Smith', 'programmer')) 
employers.append(make_employer('Brad', 'Pete', 'driver')) 
employers.append(make_employer('Julia', 'Robertson', 'artist')) 




