#u wana use a property when u wanna make sure that an attribute has a specific value
# based on some constraints, So u wanna ensure that anything outside cannot modify this attribute
# or access this attribute inappropriately or incorrectly

class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this is invalid!")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

    salary = property(get_salary, set_salary)



p = Person("Tim")
# p.set_salary(100)
p._salary = -100
print(p.salary)











class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0
    
    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this is invalid!")
        self._salary = salary



p = Person("Tim")
# p.set_salary(100)
p._salary = -100
print(p.salary)









class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second

    # second = property(get_second, set_second) old way but we have to change names and positon

t = Time(54)
t.second = 59   #t.second = 61 or 0 etc will raise Exception
print(t.second)