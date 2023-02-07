'''Interface is really like an abstract class, except it contains only abstract methods.
So an Interface contains no implementation details whatsoever. It has no code other than the defination of methods.
And then it will raise the not Implemented error inside of every single one of those methods.

So, the point of an interface is to just outline and describe all of the methods that anything that 
inherits from that interface or implements the interface must implement.

Interfaces are very useful in Java.  In Pyhton it's not trully an interface, it is just kind of a specialized class

We can't probhit people from actually making an instance of class but we know based on the convention in Python, that we
are not going to do that because we named it abstract.
'''

''' we can determine if a class is INTERFACE if you see it does n't have any implemented methods. i.e., all the methods are abstract
(like def print_name(self):
          print() #this method is actually doing something.
          ) 
so they don't have an implementation or they raise the not implemented error.'''

# RunCodeInterface is meant to be used by things that are runnable.



class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement compile_code().")

    def execute_code(self):
           raise NotImplementedError("You must implement compile_code().")
    #these are simply kind of boiler plate they are here just to denote, that 
    # anything that implements this needs to implements these methods.

# a class is going to implement an interface, that is actually the proper terminology 
# for 


class GoCode(RunCodeInterface): #here RunCodeInterface is not a parent class so we are not calling the parent class
    def compile_code(self):     # but we are implementing the Interface. if it does then we would put it first then the 
        print("Compile Go Code") # Interface (e.g., class Code
                                   #                class GoCode(Code, RunCodeInterface)  )

                                        #(if we will not write this method for example)
    def execute_code(self):             #hey, this class influenced the interface but it didn't implement this method
         print("Execute Go Code")       # and it will tell you, you have to implement that method.



class JavaCode(RunCodeInterface):
    def compile_code(self):
         print("Compile Java Code")

    def execute_code(self):
         print("Execute Java Code")


    def test(self):
        print("test")

# both of the classes implement this interface, the reason they implement is 
# they implement all of the methods in the interface.


# type hint => ":"

def run_code(code : RunCodeInterface): #it means that I'm accepting any object that implements the RunCodeInterface.  So, It doesn't necessarily have to be code, but it has to implement this interface(RunCodeInterface.)
    code.compile_code()    #python is a weekly type lang that means the type of objects does
    code.execute_code()    # not matter but we will still try to run the methods on them,
    code.test()            # even if they dont have that method.


''' 
in prog lang like Java the parameters of the function run_code are (run_code(int, code), i.e., type and the name of the parameter)
but in python we would make this "RunCodeInterface" type
'''

go = GoCode()
run_code(go)

java = JavaCode()
run_code(java)


'''
Summary: Create an abstract class that only contains abstract methods that need to implemented by anything that inherit from.
'''



def run_code(code : RunCodeInterface): # here we are saying the parameter "code" needs to be of this type that is RunCodeInterface.
    code.compile_code()                 # so now If i pass any object to this function e.g., => code.compile_code()
    code.execute_code()                 # I know it's going to be of type, RunCodeInterface. So i know i can
    code.test()                         # use these    class RunCodeInterface:
                                                            # def compile_code(self):
                                                           #     raise NotImplementedError("You must implement compile_code().")

                                                            # def execute_code(self):
                                                            #     raise NotImplementedError("You must implement compile_code().")  
                                                            # 
                                                            #   methods on it



'''
1. Interfaces, like abstract classes, should not be instantiated. There are meant to act as an abstract data type that classes will implement.

2. Intefaces should only contain abstract methods: 

Unlike abstract classes the only methods allowed in an interface are abstract. 
An interface does not provide any concrete methods or behavior. 

3. Purpose of an Interface:
  a) To specify the methods a class should implement.
  b) To act as a blueprint for a class that decides to implement it.

  An interface is an abstract data type that is meant to be implemented by a class.
  Any class that implements(in Python, inherits) an interface must implement all of 
  the methods defined in the interface. This makes the interface act like a blueprint 
  for the class. Interfaces provide no concrete implementations and do not redudce the
  amount of code needed for classes implementing them.

'''
                                                                                                        