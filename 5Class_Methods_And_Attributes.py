class Car:
    numbers_of_cars = 0
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # self.numbers_of_cars = 1 #(now i will get = 1 from  print(c1.numbers_of_cars) because then i'll be accessing the instance attribute not the class attribute.)
        Car.numbers_of_cars += 1 # i am modifying the class attribute by using the class name and adding one to it.

    @classmethod #put always for class methods with first parameter as cls
    def update_number_of_cars(cls, cars): #cls is the name of the class i.e., Car and cars is just parameter that i am passing to this method to update the number of cars with.
        cls.numbers_of_cars = cars #if we put 5 instead of cars it will print 5 instead of 10 but remove the parameter cars from above line
        print("run")


# Car.numbers_of_cars += 3

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

# print(c1.numbers_of_cars) #gives me class attribute not the instance attribute. if i have number_of_cars as an attribute on my instance, I would get that but
                            # since i don't have that, I am just getting the class attribute, So I can access the class attribute from instances but it is not preffered to this way
                            #and the value is same for c2.number_of_cars

# print(c1.numbers_of_cars)
# print(Car.numbers_of_cars)

print(c1.numbers_of_cars)  
print(c2.numbers_of_cars)     
print(Car.numbers_of_cars)    




#print statement for class methods.

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

Car.update_number_of_cars(10)

print(c1.numbers_of_cars)  
print(c2.numbers_of_cars)     
print(Car.numbers_of_cars)











class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)

print(Circle.perimeter(4))
print(Circle.get_area_and_perimeter(4))


# In Python, class attributes are attributes associated with a class, not an instance of a class. 
# Class attributes can be accessed by using the class name or from any instance of the class.



"""A instance method can access and 
modify both class and instance attributes while a class method can only access and modify class attributes.

Class methods are used when you only need access to class attributes 
or class methods while instance methods are used when you need access to instance attributes or instance methods.


Class methods accept a mandatory cls parameter 
and are denoted using the @classmethod decorator, while instance attributes accept a mandatory self parameter. 
Class methods don't have access to an instance and therefore, 
can only modify and access class attributes and can only call other class (or static) methods. 
Instance attributes have access to an instance and can modify and 
access both instance and class attributes as well as call any other methods defined in the class."""


class Person:
  population = 0

  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.population = 1
      Person.population += 1

p1 = Person("Tim", 100)
p2 = Person("Clement", 54)

x = Person.population
print(x)

# ans x = 2
# This is because Person.population references the class attribute population, 
# while self.population references the instance attribute associated with each new instance of the Person class. 
# Both  p1 and p2 have their own  population attribute which are equal to 1, 
# while the Person class has it owns separate  population attribute.