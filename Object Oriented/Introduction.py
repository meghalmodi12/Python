class Parrot:

    #class level attributes
    species = 'bird'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return '{} is sings {}'.format(self.name, song)

    def dance(self):
        return '{} is dancing'.format(self.name)

Blu = Parrot('Blu', 10)
Woo = Parrot('Woo', 15)

#Accessing class level attributes
print('{} is a {}'.format(Blu.name, Blu.__class__.species))

#Calling methods
print(Blu.sing('Happy'))
print(Woo.dance())
