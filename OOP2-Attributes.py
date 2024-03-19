class SedanCar:
    # Class Attribute
    zarfiat = 5

    # Instance Attribute
    def __init__(self, horsepower):
        self.hp = horsepower


# Accessing class attribute
# print(SedanCar.zarfiat)

# Creating instances
persia = SedanCar(130)
dena = SedanCar(135)

# Accessing instance attribute
# print(persia.hp)
# print(dena.hp)

# Modifying instance attribute
# persia.hp = 140
# print(persia.hp)
# print(dena.hp)

# Modifying class attribute
SedanCar.zarfiat = 4
print(persia.zarfiat)
print(dena.zarfiat)
