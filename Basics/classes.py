students = []

class Student:

    dept = "DWS"

    def __init__(self, name, id):
        self.name = name
        self.id = id         
        students.append(self)

    def get_name(self):
        return self.name

    def get_dept(self):
        return self.dept

class HighSchoolStudent(Student):
    pass

"""
student = Student("selim", 1)    
print(student.name)
print(student.get_name())
print(student.dept)
print(student.get_dept())
print(Student.dept)

highSchoolStudent = HighSchoolStudent("selim", 2)
print(highSchoolStudent.get_name())
"""