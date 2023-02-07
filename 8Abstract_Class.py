# An abstract method is a method that is defined in a interface or abstract class and does not provide an implementation.
# Abstract methods are designed to be overriden by base or subclasses that extend the class or implement the interface they're defined in.

#Abstract Class
#An abstract class is a class that contains at least one abstract method and is not meant to be instantiated. 
# Abstract classes are meant to act as the parent or base class in an inheritance hierarchy. 
# Typically abstract classes implement some functionality that can be used commonly by all child or subclasses.

# abstract method is a method that is not yet implemented by this class, but that is required to be implemented
# by any class that inherits from it.

import random
class AbstractGame: # what makes it an abstract class is the fact that we should never instantiate this.
    def start(self): # it is also an instance method cuz if i'm gonna access another method, then I need access to either the "cls" the class name or the instance
                        # and if it's gonna be an instance method that I want access to, well I need access to the instance
                        #ALSO start method relies on the play method of both of these classes to actually implement the game.
        while True:
            start = input("Would you like to play")
            if start.lower() == "yes":
                break

        self.play()
 
    def end(self): #I do want to access to self cuz this reset method will be an instance method and since that's an 
        print("The game has ended.")      # instance method and to be able to call the instance method, I need access to the instance
        self.reset()                        # so i have a self.


# Now I need a Abstract method
# Abstract method is a method that's need to be implemented by any class,
# that inherits from this abstract game class.


#we are going to use the abstract method inside of the abstract class.
# but they only work when we have a concrete instance or a concrete implementation of this class or of this method.


    def play(self):
        raise NotImplementedError("You must provide an implementation for play()") # if we try to call ''play'' and it has not been implemented the error will be raised.
                                    # we want a child class (i.e., derived class) of this abstract game class to implement this method
                                    #so anything that inherits from "AbstractGame" needs to override this method and provide an implementation for it.


    def reset(self):
        raise NotImplementedError("You must provide an implementation for play()")


# as start and end exist. However, we need whoever inherits from this to give us play and to give reset. The point of this is, this kind of provides
# a framework for every game. "Play and  reset " need to be implemented by the game, as they are specif to each game, if not then the error will be raised.
# so Play and reset are Abstract Method




class AnotherGame(AbstractGame):
    pass




class RandomGuesser(AbstractGame):  # we have implemented from AbstractGame, but there is no constraint on this constructor, So we can make this game however we want.
    def __init__(self, rounds):     # the only thing is we need to implement play and reset.
        self.rounds = rounds
        self.round = 0


    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")
            random_num = random.randint(0, 10)
            while True:
                guess = input("Enter a number between 1-10:")
                if int(guess) == random_num:
                    print("You got it!")
                    break

        self.end()

# game = RandomGuesser(2)
# game.start()

# games = [RandomGuesser(1), AnotherGame()]

# for game in games:
#     game.start()

games = [AnotherGame(), RandomGuesser(1)]

for game in games:
    game.start()





''' start and end method rely on the fact that play and reset method is defined, Now since AbstractGame is an Abstract Class, we can't really define a play or a reset method,
because this is AbstractGame, it just says I am a game, I don't know what type of game I am. I am just some game. So you need to tell me what type of game I am by defining the reset method
and the play method If you decide to inherit from me, As play and reset are abstract methods as they are not implemented And we try to use them, we will get a not implemented error, that means we need to override them inside of a class that
is going to inherit from this abstract class.
RandomGuesser is a concrete class'''



'''An abstract class is designed to act as the base class in an inheritance hierarchy and is not designed to be instantiated. Abstract classes usually contain abstract methods that are meant to be implemented by classes that inherit from them.

All method types are allowed in an abstract class. Abstract classes usually contain some concrete methods (ones that provide an implementation) while also defining abstract methods that must be implemented by child classes that inherits from it.

In many other programming languages it is enforced that a subclass of an abstract class must implement any abstract methods it contains. However, in Python this behavior is not enforced and although it is conventional for subclasses of an abstract class to do so it is not required.'''





'''Answer

 To function as a base class that provides already implemented behavior that can be extended by any subclasses to create a full implementation.
Explanation

An abstract class should not be instantiated and is meant to function as a base class that provides already implemented behavior
 that can be extended by any subclasses to create a full implementation. Abstract classes often contain abstract methods that are meant to be 
 implemented by any subclasses to create a full implementation of the abstract class.'''