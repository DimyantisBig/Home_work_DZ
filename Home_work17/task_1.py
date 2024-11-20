class Animal:
    def talk (self):
        pass

class Dog (Animal):
    def talk(self):
        print('Dog sey Wof-wof!')

class Cat (Animal):
    def talk(self):
        print('Cat sey Myau - myau!')

def make_animal_talk (animal):
    animal.talk()

d = Dog ()
c = Cat ()

make_animal_talk (d)
make_animal_talk(c)


