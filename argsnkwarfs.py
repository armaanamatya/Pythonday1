# [*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. 
# Test your function with various input cases.

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

sum = sum(8,9)
print(sum)    

#[**kwargs] Create a function create_student_report that takes the student's name as the first argument, the student's age as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. 
# The function should return a dictionary with the student's information and a list of subjects along with their scores.    

def create_student_report(name,age,**kwargs):
    student_info = {
        "name": name,
        "age": age,
        "subjects": []
    }

    for subject, score in kwargs.items():
        student_info["subjects"].append({subject : score})

    return student_info

sujs = {"Social" : 50, "Math" : 60, "Science" : 70}

student_report = create_student_report("Armaan", 19, **sujs)

print(student_report)