class Animal:
    def __init__(self,color):
        self.color = color

class Dog(Animal):
    def Make_A_sound(self):
        return("'WOOF!'sound")

class Cat(Animal):
    def Make_A_sound(self):
        return("'MEOW' sound")


dog_1 = Dog("Brown")
cat_1 = Cat("White")

print("This dogs color is: ", dog_1.color)
print("And this dog is making a",dog_1.Make_A_sound())

print("This cats color is: ", cat_1.color)
print("And this cat is making a",cat_1.Make_A_sound())
