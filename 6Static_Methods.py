#these are like a function that sits Inside of a class. It has a no Access to any of the Instance Atttributes
# or to the Class Attributes. We simply use it like a function.

class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    @staticmethod
    def average_from_grades(grades):  #no mandatory first parameters
        return sum(grades) / len(grades)

s1 = Student("Aamir", [80, 78, 99, 88])
s2 = Student("Ali", [81, 98, 79,  78])

average = s1.average_from_grades(s1.grades)  #average_from_grades does not have access to my
print(average)                               # student's grades because it is not an Instance attribute
                                             #so we need to pass s1.grades.


average = s1.average_from_grades(s2.grades)   #we can call "s1.average_from_grades" or "s2.average_from_grades"
print(average)                                  # or we can call directly on Student class itself "Students.average_from_grades"

# now a valid question that why don't we change it to a instance method like this
# 
# def average_from_grades(self):
#         return sum(self.grades) / len(grades)

# because  we might want to use it not on an instance of this class or i might wanna modify the grade slightly 
# before I use this method.
# maybe I wanna only look at the first two grades ""average = s1.average_from_grades(s2.grades[:2])""

#or s1.average_from_grades(s2.grades + s1.grades)

#if we had used instance method it would just look at all of the grades inside of the student and I would need to
# change the grades list.

# it is related to student class but we don't wanna directly be accessing the attributes from each student.









class Student:
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades


    def average(self): #we have no decorator over top of it.
        return sum(self.grades) / len(self.grades)


    @classmethod
    def average_from_grade_plus_bump(cls, grades):
        average = cls.average_from_grade(grades) # from inside here, we could use the static method(avg_from_grades) because we have access to the class
        return min(average + cls.grade_bump, 100)

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades) #theoretically, inside of the static method, we can still access the class attributes(e.g., grade_bump), class methods or other static methods
                                         # we could do something like ""Student.grade_bump"" because it is supposed to just act like function and not rely on anything from outside of the function  
                                         # like class attribute(grade_bump) or class methods, so it should just work indepedently of everything else. 

        #the main difference btw the static method and the class method is that class method has access to
        # things related to the class(class attributes and other class methods and static methods that are a part of the class)


        #if u find that inside of the static method you need to access the class attributes or other class methods then instead you should change this to a 
        # class method and get access to the cls keyword and then use that instead of the class name directly to access other methods or attributes.