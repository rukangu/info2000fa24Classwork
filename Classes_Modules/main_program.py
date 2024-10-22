# we will get student details and welcome them
# university, name, major,

from students import Student
# def get_name():
#     name = input("Name: ")
#     return name

# def get_major():
#     major = input("major: ")
#     return major

# def get_university():
#     uni = input("university: ")
#     return uni

def get_student():
    name = input("Name: ")
    major = input("major: ")
    uni = input("university: ")

    return Student(name, major, uni)

# # call the functions
# user_name = get_name()
# user_major = get_major()
# user_university = get_university()

# new simple function
# my_student = get_student()


def main():
    my_student = get_student()

    # greet the student
    print (f"Hello {my_student['name']}. I hope you like going to {my_student['university']}, for {my_student['major']}!")

    # print (f"Hello {my_student[0]}. I hope you like going to {my_student[2]} for {my_student[1]}!")
if __name__ == "__main__":
    main()
