class animal:
    def sound(self):
        print('Animal makes sound')
class bird(animal):
    def show(self):
        print('Bird makes pew pew sound')
obj = bird().show()
obj1 = animal().sound()