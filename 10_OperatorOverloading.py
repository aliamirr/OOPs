#Operator Overloading is oura ability to implement custom operations on 
# our own classes.

# you can make your custom objects, kind of act like built-in objects in Python
# by implementing these operations.

#any operation you see you can probably implement yourself on your own class.
# just look up the appropriate dunder or magic method.
import math
class Page:
    def __init__(self, words,  page_number):
        self.words = words
        self.page_number = page_number

    #we have our own object which is left operand(self(page1)), then 2nd object we need is a parameter which is right operand(other(page2)) 
    def __add__(self, other):
        new_words = self.words + " " + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page("A is great instructor!!!", 1)
page2 = Page("This is another page!!!", 2)
page3 = page1 + page2
print(page3.words, page3.page_number)












class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.after_tax_price = 0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.TAX), 2)


    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)


    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)


bread = StoreItem("Bread", 7)
# discounted_bread = bread - 2
discounted_bread = bread * 0.5
print(discounted_bread.after_tax_price)











class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # def __truediv__(self, factor):   #(__floordiv__) is integer div.
    #     new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
    #     new_point2 = (self.point2[0] / factor, self.point2[1] / factor) 
    #     return Line(new_point1, new_point2)

    # def __floordiv__(self, factor): 
    #     new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
    #     new_point2 = (self.point2[0] // factor, self.point2[1] // factor) 
    #     return Line(new_point1, new_point2)



    

    def __len__(self):
        distance_x = ((self.point1[0] - self.point2[0]) ** 2)
        distance_y = ((self.point1[1] - self.point2[1]) ** 2)
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)


    def __eq__(self, other):
        if not isinstance(other, Line): #if other is not the instance of Line Class then return False.
            return False

        return self.point1 == other.point1 and self.point2 == other.point2
    
    def __ne__(self, other):
        return not self.__eq__(other)


    def __gt__(self, other):
        return len(self) > len(other)


    def __ge__(self, other):
        return len(self) >= len(other)


    def __lt__(self, other):
        return len(self) < len(other)


    def __le__(self, other):
        return len(self) <= len(other)







line1 = Line((10, 5), (20, 9))
line2 = Line((20, 5), (20, 9))
# line1 = line2 #because line1 and line2 are exact same object. if we dont do this then line1 and line2 are two seprate objects that have same value/properties.


print(line1 > line2) #line1 is self and line2 is other.



print(line1 == line1)
print(line1 == line2) # the reason we are getting false is as when we compare with two equal signs
print(line1 is line2)                      # and not implemented the double equal sign operation or the double equal sign dunder method
                      # we are actually going to compare and check if these two objects are the exact same.

# line2 = line1 / 2
# line2 = line1 // 2
# print(line2.point1, line2.point2)
# print(len(line1))










class Page:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return self.text

    def __str__(self):  # it is used fo a string readable / human readable kind of version of our object.
        # return f"Page(text = {self.text}, page_number =  {self.page_number})"
        return f"Page({self.text}, {self.page_number})"


    def __repr__(self):          #this is meant to represent the internal representation of an object.
        return self.__str__()    # with repr we give all of the important information about the object
                                 #  that we need when we are debugging or when we're looking at the internal
                                 # representation of it. 



class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)

    def __str__(self):
        output = f"Book({self.title}, {self.author}, {self.id_number})"
        
        for page in self.pages:
            output += "\n" + str(page)

        return output

    def __repr__(self):
        return f"Book(id_number = {self.id_number})"

page1 = Page("Page 1!", 1)
page2 = Page("This is page 2!", 2)
book = Book("A|CS is Great", "A|A", [page1, page2], 1)
print(len(page1))
print(len(page2))
print(len(book))

print(page1, page2)

print(book)

print(repr(book))

print([1,2,3,4])
print(repr(True))


'''
1. In Python, you can explicitly call a dunder method. 
For example, you could do something like this: x.__init__(1, 2, 3)?

ANSWER: TRUE: Dunder methods are just like other methods except they can be triggered in unique ways. 
For example, the __init__ dunder method will automatically be called when instantiating a new object.

2. In Python, when calling the str() function on an instance of a class the __str__ method will be called. 
The  __str__ is designed to return the string representation of an object.


3. In Python, calling the print() function on an instance of a class will call which of it's dunder methods?

ANSWER:   In Python, when calling the print() function on an instance of a class the __str__ method will be called. 
This is because behind the scenes the print() function explicitly calls the  str() function 
on all of it's arguments before printing them.

4. In Python, the __repr__ method is used for debugging and displaying meaningful information about the object. 
It is not designed to provide a string representation that is useful for printing.
'''