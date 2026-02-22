class Student():
    def __init__(self,name,lasname, age):
        self.name = name
        self.lasname = lasname
        self.age = age
    def get_info(self):
        print(self.name,self.lasname,)


class School():
    def __init__(self,schoolname,adress):
        self.schoolname = schoolname
        self.adress = adress
        self.students = []


    def add_student(self,add_student):
        self.students.append(add_student)

    def remove_student(self,remove_student):
        self.students.pop(remove_student)

    def show_students(self):
        print(self.students)

student = Student("saxeli","gvari",22)
student.get_info()

school = School("sulxan kvernadze ","sadgac")

school.add_student("kaci 1")

school.add_student("kaci 2")
school.add_student("kaci 3")

school.remove_student(0)
school.show_students()
