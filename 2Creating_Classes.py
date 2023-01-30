class Person: #this is now a new data type in our program.
    def __init__(self, name, age): # init will automatically called when ever we create a new instance
        self.name = name  # instance.name , we are making new attribute
        self.age = age # these are attributes on these instances
        #self is acess to ths instance "p1 = Person("Tim", 21)"
        #self is access to the atribute(p1) itself.
        #self is a parameter that needs to be in all of your methods but specially this init method, and this references the instances of the class.

    #so u can think of the self as being p1 or self being p2, so we are accessing the instance ourself that this method is acting on in creating a new attribut on that instance called name which is equal to name.


        # attribute is the data associated with an instance of an object.
p1 = Person("Tim", 21) # we initiliaze this class,then the init method runs and we print whatever
p2 = Person("Bill", 26)  # the name and age are required to initialize this instance.        # new instance of the person type



print(p1.name, p1.age) # accessing the attributes (p1.name/p1.age , so i just write what the name of the attribute is,)
print(p2.name, p2.age)

# p1.new = "random"

p1.name = "random" # that is how u modify/create attributes outside of the class. Whatever are we doing with self inside we are doing that with the p1.name  = random

print(p1.name)