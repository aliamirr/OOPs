class Person: #Person is => "Super, Base, Parent Class."
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.second_name}")

class Employee(Person): #Employee is => "Child, Derived, Sub Class" , Employee has access to everything inside of it's super class. 
    def test(self):     # but not vice versa
        print("test")

# e = Employee("Tim", "Programmer")
e = Person("Tim", "Programmer")
e.say_hello()
# e.test()  #we cannot call e.test() as this method is defined inside of a employee
            #not inside of a person, because person does not inherit from employee. so it does n't have access to what inside of employee,


e = Employee("Tim", "Programmer")
e.say_hello()
e.test() # now it works.













#sometimes there is stuff in "Person" that we don't want or we wanna change the way that it works. e.g., say hello method
# the way we can do this is we would override the method inside of the child class, so the derived class



class Person: 
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.second_name}")



class Employee(Person):
    def say_hello(self): # here i have overridden the parent class. #it is now changed for Employee class, and when u class say_hello we are goin 
                            #to use the method defined here not in the Person class
        print("--------")
        super().say_hello()   #super gives you access to parent class |||| implicitly (invisibly) we will pass self keyword to the say_hello method that's on our super class
        print("--------")

p = Person("Joe", "Schmo")
p.say_hello()
e = Employee("Tim", "Programmer")
e.say_hello()



















class Person: 
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.second_name}")


class Employee(Person):
    def __init__(self, first_name, second_name, salary):
        super().__init__(first_name, second_name) #in python whenwver u override the parent constructor of your superclass you mandatory/manually need to call constructor/"super()"
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")

class Manager(Employee):
    def __init__(self, first_name, second_name, salary, department):
        super().__init__(first_name, second_name, salary)
        self.department = department

class Owner(Person):
    def __init__(self, first_name, second_name, net_worth):
        super().__init__(first_name, second_name)
        self.net_worth = net_worth


# m = Manager("Tim", "Programmer", 500000, "Sports")
# m.say_hello
 
o = Owner("Owner", "Programmer", "Sports")
o.say_hello()
print(type(o))
print(isinstance(o, Person))

m = Manager("Mann", "Programmer", 500000, "Sports")
print(isinstance(m, Person))

m = Manager("Mann", "Programmer", 500000, "Sports")
print(isinstance(m, Employee)) #or similiarly we can see for Manager.

m = Manager("Mann", "Programmer", 500000, "Sports")
print(isinstance(m, Manager))

m = Manager("Mann", "Programmer", 500000, "Sports")
print(isinstance(m, Owner))







 
class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A,B):
    pass

c = C() # it looks if C has init method if it has then we use it, if not then we go to A and similarly
        # if A doesn't have then we go to B








class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A,B):
    def __init__(self):
        super().__init__() #super keyword is going to reference A but if A doesn't have the method we are looking for
                            # then it's gonna reference B
c = C()


#this is know as Method Resolution Order of method in Classes
# it is only in python u can't have multiple inheritance

# and it is complicated because you have to have a set way of knowing
# which super class we should actually be looking in.

# it gets even more complicated when other classes are also inheriting
# from multiple other classes(i.e., layers of multiple inheritence)

#so summary is we look in main class, then super class, then second super class.













class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A,B):
    def __init__(self):
        super().__init__() 

c = C()
print(isinstance(c, A))


# if we check C is an instance of A, that will be true and
# if we check C is an instance of B, that will be true










#DUCK TYPING



class Duck:
    def swim(self):
        print('Swimming duck')

    def fly(self):
        print("Flying duck")

class Whale:
    def swim(self):
        print("Swimming whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    animal.fly()




