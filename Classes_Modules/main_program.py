# we will get student details and welcome them
# university, name, major,

# from students import Student
# from logger import Logger
from utils import Logger, Student
import random

def get_student():
    name = input("Name: ")
    major = input("major: ")
    uni = input("university: ")
    return Student(name, major, uni)

def main():
    # create  a logger object
    my_logger = Logger()
    for _ in range(2):
        my_student = get_student()
        # my_student.university = "Alabama"
        my_student.grades = [random.uniform(0,100) for _ in range(5)] # generate 5 random grades
        my_logger.logRow(str(my_student))
    # greet the student
    # print (f"Hello {my_student.name}. I hope you like going to {my_student.university}, for {my_student.major}!. Grade: {my_student.compute_letter_grade()}")
if __name__ == "__main__":
    main()
