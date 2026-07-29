class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, major, student_id):
        super().__init__(name, age)

        self.major = major
        self.student_id = student_id

    def study(self, hours):
        print(f"{self.name} studied for {hours} hours.")

    def Change_major(self, new_major):
        self.major = new_major

    def graduate(self):
        print(f"{self.name} has graduated.")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)

        self.subject = subject
        self.salary = salary

    def grade_assignment(self):
        print(f"{self.name} has graded assignment")


    def assign_homework(self):
        print(f"{self.name} assigned homework.")


#________________
# Student objects
#________________


student1 = Student("Ali", 21, "CompSci", "1001")
student2 = Student("Ant", 21, "BM", "2002" )

#________________
#student methods
#________________


