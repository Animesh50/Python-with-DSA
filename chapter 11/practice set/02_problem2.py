class Animals:
    pass

class Pet(Animals):
    pass

class Dog(Pet):

    @staticmethod
    def bark():
        print("Bow Bow!!")

d = Dog

d.bark()