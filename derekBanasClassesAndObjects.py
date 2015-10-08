import sys
import os

class Animal:
    __name = ""
    __height = 0                # __ means variable is PRIVATE
    __weight = 0
    __sound = 0


    # Constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

 # Setters and Getters    # Setters and Getters
    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_height(self, new_height):
        self.__height = new_height

    def get_height(self):
        return self.__height

    def set_weight(self, new_weight):
        self.__name = new_weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, new_sound):
        self.__name = new_sound

    def get_sound(self):
        return self.__sound

 # ^^ Setters and Getters    # Setters and Getters

    def get_type(self):
        print("Animal")

# !!! Formatting
    def about(self):
        return "{} is {} cm tall and {} kilograms and says \" {} \" ".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound)

# Creating an object

cat = Animal("Lizzy", 30, 15, "Meow")

print(cat.about())


# INHERITANCE

class Dog(Animal):
    __owner = ""                # variable specific to Dogs

    # Overwriting Constructor (making it more specific for Dogs)
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)          # variables handled by superclass constructor


    # Setter for the Dog-specific variable
    def set_owner(self, owner):
        self.__owner = owner

    # Getter
    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # Overwriting the 'about' method
    def about(self):
        return "{} is {} cm tall and {} kilograms and says \" {} \" to its owner {} ".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound,
                                                                      self.__owner)

    # method overloading

    def multiple_sounds(self, how_many):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)



musya = Dog("Musya", 20, 10, "Woof", "Marina")

# print(musya.about())

print(musya.get_name())

print("\n")




# POLYMORPHISM.   Correct Functions are Chosen automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(musya)

musya.multiple_sounds(4)