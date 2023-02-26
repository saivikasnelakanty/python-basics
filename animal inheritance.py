class Animal:
    def __init__(self, animal_name, animal_type):
        self.animal_name = animal_name
        self.animal_type = animal_type

    def animal_group(self, group):
        return(group)
    
    def animal_sound(self, sound):
        return(sound)
    
obj_Animal = Animal("Crocodile", "Canivores")
print(obj_Animal.animal_name, obj_Animal.animal_type)
print(obj_Animal.animal_group("Wild Animal"), obj_Animal.animal_sound("Hiss"))

class cat(Animal):
    pass
obj_cat = cat("cat", "Carnivores")
print(obj_cat.animal_name, obj_cat.animal_type)
print(obj_cat.animal_group("Domestic Cat"), obj_cat.animal_sound("Meow"))

class Dog(Animal):
    pass
obj_Dog = Dog("Dog", "Herbivores")
print(obj_Dog.animal_name, obj_cat.animal_type)
print(obj_Dog.animal_group("Domestic Dog"), obj_Dog.animal_sound("Barking"))
