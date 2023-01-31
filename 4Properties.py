#u wana use a property when u wanna make sure that an attribute has a specific value
# based on some constraints, So u wanna ensure that anything outside cannot modify this attribute
# or access this attribute inappropriately or incorrectly

# In object oriented programming, getters are used to return the value of attributes while setters are used to set the value of attributes. 
# Both allow you to hide complexity by providing a single method that can be used to validate data before assigning it to an attribute (setter) or mutate data (e.g. rounding a number) before returning it (getter). 
# Setters may also constrain an attribute value by only allowing you to set it to something considered valid by the class (e.g. you can't set a negative salary for an employee).



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