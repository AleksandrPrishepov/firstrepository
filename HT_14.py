# HT_14

class Dog:

    def __init__(self,  height, weight, name, age,master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        return f"Собака по имени {self.name } прыгнула, ее возраст {self.age}"
    def run(self):
        return f"Собака по имени {self.name} бежит, ее вес {self.weight}"
    def bark(self, volum):
        return f"Собака по имени {self.name} лает с громкостью {volum} децибел"
    def change_name(self, new_name):
        self.name = new_name
        return self.name



dog1 = Dog("Овчарка", 20, "Джэк", 3,"ok")
# HT_14_1
print(dog1.jump())
print(dog1.run())
print(dog1.bark(100))

# HT_14_2
print(dog1.name)
print(dog1.change_name("Шарик"))
print(dog1.__dict__)