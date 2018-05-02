class Animal:
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        print(self.health)
        return self
    def run(self):
        self.health = self.health - 5
        print(self.health)
        return self
    def health(self):
        print(self.name,self.health)
        return self
animal = Animal("Wrigley")
animal.walk().walk().walk().run().run()
class Dog(Animal):
    def __init__(self,name):
        super().__init__(self,name)
        self.health = 150
        self.name = name
    def pet(self):
        self.health += 5
        return self
dog = Dog("Pepsi")
dog.walk().walk().walk().run().run().pet()
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(self.name)
        self.health = 170
        self.name = name
    def fly(self):
        self.health -= 10
        return self
    def health(self):
        print(self.name,self.health)
        return self
        print("I am a Dragon")
dragon = Dragon("Eregon")
dragon.run().fly().health()

