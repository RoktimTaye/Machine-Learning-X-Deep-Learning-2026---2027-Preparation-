class Animal:
    def __init__(self,sound):
        self.sound = sound
class Bird(Animal):
    def display(self):
        print(f"Bird Makes Sound like {self.sound}")