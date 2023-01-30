#just like function we can return values in methods, and they have access to the attributes of whatever instance they're bieng called on.

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None


    def say_hello(self):  #because methods acts on a instance of a class, self stores that instance, so you need self as the very first parameter.
        print(f"Hello, {self.name}") # here I'm accessing the name attribute of whatever instance this method is being called on and I am printing it out.
    
    def set_age(self, age):
        self.age = age #it is setting the value of an attribute. its taking age and it's then creating a new attribute called age and associating with whatever the age is, that we added in.

    def get_age(self):
        return self.age  #used mostly in other programming languages. #getter method is a method that gives you of an attribute. in python these are redundant as we can directly access the attribute directly by just referencing age.


p1 = Person("Tim")
p2 = Person("Susan")
p1.set_age(21)
p1.say_hello()
p2.say_hello()
print(p1.age)
p1.set_age(24) #we can directly use p1.age(24)
p1.get_age()










class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked
        #or
        # if self.locked == True:
        #     self.locked = False
        # else:
        #     self.locked = True

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")



counter = Counter()


counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.print_count()

counter.toggle_lock()
counter.decrement()










class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked # we are tooggling the lock.
        #or
        # if self.locked == True:
        #     self.locked = False
        # else:
        #     self.locked = True

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked: # we are looking at the lock
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")
    #increment,decrement or print count all of these methods don't return anything, but we could return something from them. most of these are modifying an attribute on this object
    #these are called instance methods, they all take in self parameters and then they have access to all of these attributes.


counter = Counter()
counter2 = Counter()


counter.toggle_lock()
counter2.increment()
counter.print_count()
counter2.print_count()



