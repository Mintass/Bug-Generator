class Course:
    
    def __init__(self, course_id, course_name, department, credits, time, location, registered_students:list, grade_table:dict):
        self.course_id = course_id
        self.course_name = course_name
        self.department = department
        self.credits = credits
        self.time = time
        self.location = location
        self.registered_students = registered_students
        self.grade_table = grade_table
        
    def select_attribute(self):
        attributes_list = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith('__') and not attr.endswith('__')]
        while True:
            selected_attribute = input(f'Which attributes do you want to change in {self.course_name}? ')
            if selected_attribute not in attributes_list:
                if str(input('Illegal attributes, do you want to input again? (Y/n) ')) == 'n':
                    return
                continue
            return selected_attribute
            
    def add_student(self, student):
        self.registered_students.append(student.student_id)
        
    def del_student(self, student):
        self.registered_students.remove(student.student_id)

class CourseManagement:
    
    def select_course():
        while True:
            course_id = int(input('Please input course id: '))
            selected_course = next((c for c in course_list if c.course_id == course_id), None)
                
            if selected_course is None:
                if str(input('Illegal course id, do you want to input again? (Y/n) ')) == 'n':
                    return None
                continue
            return selected_course
    
    def register_course(selected_course, selected_student):
        if selected_student.student_id in selected_course.registered_students:
            print(f'You are already registered for {selected_course.course_name}')
            return
        Course.add_student(selected_course, selected_student)
        Student.add_selected_course(selected_student, selected_course)
        print(f'You have successfully registered for {selected_course.course_name}')
    
    def delete_course(selected_course, selected_student):
        if selected_student.student_id not in selected_course.registered_students:
            print(f'You are not registered for {selected_course.course_name}')
            return
        Course.del_student(selected_course, selected_student)
        Student.del_selected_course(selected_student, selected_course)
        print(f'You have successfully deleted {selected_course.course_name}')
    
    def time_sort(self):
        weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        time_tup = (weekdays[self.split(' ')[0]], self.split(' ')[-1])
        return time_tup
    
    def set_grade(self, student_id, grade):
        self.grade_table[student_id] = grade
 
class Student:
    
    def __init__(self, student_id, last_name, first_name, gender, birthday, department, selected_courses):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.birthday = birthday
        self.student_id = student_id
        self.department = department
        self.selected_courses = selected_courses
    
    def register_student():
        student_id = int(input('Please enter the student ID: '))
        last_name = input('Please enter the last name: ')
        first_name = input('Please enter the first name: ')
        gender = input('Please enter the gender: ')
        birthday = input('Please enter the birthday (format: YYYY-MM-DD): ')
        department = input('Please enter the department: ')
        
        student_list.append(Student(student_id, last_name, first_name, gender, birthday, department, []))
    
    def select_student():
        while True:
            student_id = int(input('Please input student id: '))
            selected_student = next((s for s in student_list if s.student_id == student_id), None)
            
            if selected_student is None:
                if str(input('Unregistered student id, do you want to input again? (Y/n) ')) == 'n':
                    break
                continue
            return selected_student
            
    def add_selected_course(self, selected_course):
        self.selected_courses.append(selected_course)
            
    def del_selected_course(self, selected_course):
        self.selected_courses.remove(selected_course)
        
    def query_credits(self):
        self.selected_courses.sort(key=lambda x: x.course_id)
        for j in self.selected_courses:
            print(f'{j.course_name}: {j.credits}')
            
    def query_grades(self):
        for k in self.selected_courses:
            if str(self.student_id) in k.grade_table:
                print(f'{k.course_name}: {k.grade_table[str(self.student_id)]}')
            else:
                print(f'You don\'t have grade of {k.course_name}')
        
        
Math = Course(course_id=3, course_name='Math', department='Mathematics', credits=3,
                    time='Monday 9:00-10:30', location='A101', registered_students=[4730], grade_table={'4730': 86})
English = Course(course_id=5, course_name='English', department='Languages', credits=2,
                       time='Tuesday 10:30-12:00', location='A204', registered_students=[4730], grade_table={'4730': 90})
Physics = Course(course_id=2, course_name='Physics', department='Sciences', credits=4,
                       time='Tuesday 18:30-9:00', location='B303', registered_students=[4730], grade_table={})
History = Course(course_id=4, course_name='History', department='Social Sciences', credits=3,
                       time='Thursday 14:30-16:00', location='A104', registered_students=[4730], grade_table={'4730': 69})
Art = Course(course_id=1, course_name='Art', department='Arts', credits=2,
                   time='Friday 16:00-17:30', location='B415', registered_students=[], grade_table={})
        
course_list = [Math, English, Physics, History, Art]


student1 = Student(4728, 'Smith', 'John', 'Male', '2000-01-01', 'Computer Science', [])
student2 = Student(4729, 'Doe', 'Jane', 'Female', '2000-02-02', 'Mathematics', [])
student3 = Student(4730, 'Lee', 'Minho', 'Male', '2000-03-03', 'Physics', [Math, History, Physics, English])

student_list = [student1, student2, student3]