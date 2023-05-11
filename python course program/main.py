import sys
import basic_class as basic
from textwrap import dedent 

# input 1
def register_func():
    if basic.Student.select_student():
        print('You are already registered, please input 2 to modify the courses.')
        return
    if input('Do you want to register now? (y/N) ') != 'y':
        return
    basic.Student.register_student()

# input 2
def course_modify_func():
    selected_student = basic.Student.select_student()
    if selected_student is None:
        print('Not register yet, please input 1 to register')
        return
    selected_course = basic.CourseManagement.select_course()
    if selected_course is None:
        return
    action = str(input('Register or Delete? (r/d) '))
    if action == 'r':
        basic.CourseManagement.register_course(selected_course, selected_student)
    elif action == 'd':
        basic.CourseManagement.delete_course(selected_course, selected_student)

# input 3
def course_management_func():
    selected_course = basic.CourseManagement.select_course()
    if selected_course is None:
        return
    selected_attribute = basic.Course.select_attribute(selected_course)
    if selected_attribute is None:
        return
    attributes_value = input(f'Enter the new value for {selected_attribute}: ')
    setattr(selected_course, selected_attribute, attributes_value)
    print(f'You have successfully changed {selected_attribute} to {attributes_value}')
    
# input 4
def course_schedule_schedule():
    selected_student = basic.Student.select_student()
    if selected_student is None:
        return
    if not selected_student.selected_courses:
        print('You haven\'t registered for any courses yet')
        return
    selected_student.selected_courses.sort(key=lambda x: basic.CourseManagement.time_sort(x.time))
    for i in selected_student.selected_courses:
        print(f'{i.course_name}: {i.time}')

# input 5
def query_func():
    selected_student = basic.Student.select_student()
    if not selected_student.selected_courses:
        print('You haven\'t registered for any courses yet')
        return
    user_input = input('Do you want to check grades or credits? (g/c)')
    if user_input == 'c':
        basic.Student.query_credits(selected_student)
    elif user_input == 'g':
        basic.Student.query_grades(selected_student)
    
# input 6
def exit_func():
    sys.exit()


def main():
    print(dedent("""\
        *************************************************************************
        ************** Welcome to our course registration system! ***************
        *************************************************************************
        **************    1. Registration for new user           ****************
        **************    2. Modify user course registration     ****************
        **************    3. Course management                   ****************
        **************    4. Print selected course schedule      ****************
        **************    5. Query grades and credits            ****************
        **************    6. Exit                                ****************
        *************************************************************************
        *************************************************************************"""))

    options = int(input('Input to start: '))

    if options == 1:
        register_func()
    if options == 2:
        course_modify_func()
    if options == 3:
        course_management_func()
    if options == 4:
        course_schedule_schedule()
    if options == 5:
        query_func()
    if options == 6:
        exit_func()

while True:
    main()