class Dog:
    '''A simple dog class '''
    def __init__(self,name):
        self._name = name

    def speak(self):
        return 'Woof!'
class Cat:
    '''A simple dog class '''
    def __init__(self,name):
        self._name = name

    def speak(self):
        return 'Meow!'

class Duck:
    '''A simple dog class '''
    def __init__(self,name):
        self._name = name

    def speak(self):
        return 'Cuak!!'
    

def get_pet(pet = "dog"):
    """The factory method"""
    pets = dict(dog=Dog('Hope'), cat = Cat("Peace"), duck = Duck("Happyness"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())

du = get_pet("duck")
print(du.speak())



