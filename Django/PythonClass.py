class Dog:
    
    def __init__(self, name):
        self.name = name

    def bark(self):
        print('Bark!!', self.name)

mydog = Dog('Shadow')
mydog.bark()