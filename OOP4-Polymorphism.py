class Dog():
    def sound(self):
        return "Woof!"


class Cat():
    def sound(self):
        return "Meow!"


class Cow():
    def sound(self):
        return "Moo!"


# Polymorphic method
def make_sound(animal):
    print(animal.sound())


# Create instances of different animal classes
dog = Dog()
cat = Cat()
cow = Cow()

# Call the make_sound function with different animal objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
make_sound(cow)  # Output: Moo!

# # -----------------------------------------------------------------------
#
# Polymorphism in built-in objects

t = (10, 20, 30, 40)
l = [50, 60]

# Call the __len__() method on each instance
print(l.__len__())
print(t.__len__())
