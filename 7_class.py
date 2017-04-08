class Animal():
    noise = "Talk"
    size = "Medium"
    color = "Brown"
    hair = "body hair"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise

animalObj = Animal()
print animalObj.make_noise()
print animalObj.get_color()

class Person():
    name = "Kanishka"
    color = "Brown"
    def getColor(self):
        return self.color

obj = Person()
print obj.getColor()

obj.color = "White"
print obj.getColor()
