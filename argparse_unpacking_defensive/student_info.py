# demonstrates how to pass in commandline arguments using sys and argparse

import sys
from utils import Student, Logger
import argparse

def get_student():
    ''' gets one student's information
    and returns a student class with this information'''
    name_in = input('name: ')
    major_in = input('major: ')
    uni = input('university: ')
    my_student = Student(name=name_in, university= uni, major = major_in)
    return my_student

def main():
    # print(f"You passed in {len(sys.argv)} commands")
    # print('-'*20)
    # for arg in sys.argv:
    #     print(arg)
    
    # usage: student_info.py -n number -f filename
    # if they don't pass in this flag (-n) we capture one student by default
    
    # required_students = 0
    
    # if len(sys.argv) == 1:
    #     required_students = 1
    #     # default 
    # elif sys.argv[1] == '-n' and len(sys.argv) == 3:
    #     required_students = int(sys.argv[2])
    # else:
    #     print("usage: python student_info -n Number")
        
    ####################################################################################
    # argparse 
    
    parser = argparse.ArgumentParser()
    
    # add an argument
    parser.add_argument('-n','--number', help='number of students to capture', default=1, type=int, required=True)
    
    # add file name/ path as an argument
    
    parser.add_argument('-f','--filepath',help='file path to store students', required=False, default='defaultLog.txt', type=str)
    # parse the arguments
    args = parser.parse_args()
    # create a new logger
    my_logger = Logger(args.filepath)
    
    # get a student's information and log data into file
    
    # received_student = get_student()
    # my_logger.logRow(received_student)  
    for _ in range (args.number): 
        my_logger.logRow(get_student())
    
        
if __name__ == "__main__":
    main()

