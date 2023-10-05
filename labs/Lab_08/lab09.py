import time
import math

class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")
        
    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")
    
# The attributes for each class should be as follows:

#     Orthrus
#     left: Creature
#     right: Creature
#     Cerberus
#     left: Creature
#     middle: Creature
#     right: Creature
#     Head
#     name: str'

# __str__(self) -> str
# to provide a string representation for the class
# search(self, name: str) -> bool
# a method that searches through the data structure for a specific name


class Orthrus(Creature):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} {self.right}"
    

class Cerberus(Creature):
    def __init__(self, left, middle, right):
        self.right = right
        self.left = left
        self.middle = middle

    def __str__(self):
        return f"{self.left} {self.middle} {self.right}"

class Head(Creature):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

# doggy1 = Head("Kane")
# doggy2 = Head("Wolfie")
# doggy3 = Head("Rugal")
# doggy4 = Head("Taker")
# ort1 = Orthrus(doggy1, doggy2)
# ort2 = Orthrus(doggy3, Head("Jeff"))
# cer = Cerberus(ort1, doggy4, ort2)

# print(cer)
# Kane Wolfie Taker Rugal Jeff

# cer.search("Drogon")
# False

# cer.search("Rugal")
# True