import random


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def attend_class(self, skip=False):
        if skip:
            print('Skipped class')
        else:
            print('Went to class')
    
    def add_course(self, course_name):
        self.courses.append(course_name)
    
    def __repr__(self):
        return f"<Student: {self.name}, {self.age}, {self.courses}>"


class BloomTechStudent(Student):
    def __init__(self, name, age, cohort):
        super().__init__(name, age)
        self.cohort = cohort
        self.gca_attempts = 0
    
    def take_gca(self):
        self.gca_attempts += 1

    def __repr__(self):
        return f"<BloomTechStudent: {self.name}, {self.age}, {self.cohort}>"


def student_generator():
    names = ['joe', 'anne', 'bob', 'cindy']
    cohorts = ['ds40','ds41','ds42','ds43','ds44','ds45',]
    students = []

    for x in range(30):  # 0, 1...29
        rand_name = random.choice(names)
        rand_age = random.randint(18, 99)
        rand_cohort = random.choice(cohorts)

        bts = BloomTechStudent(rand_name, rand_age, rand_cohort)
        students.append(bts)
    
    return students