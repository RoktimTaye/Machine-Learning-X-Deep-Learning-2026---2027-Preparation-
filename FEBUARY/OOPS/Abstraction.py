from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog makes barking sound.")
class Cat(Animal):
    def sound(self):
        print("Cat makes mewing sound.")
obj1 = Dog().sound()
obj2 = Cat().sound()