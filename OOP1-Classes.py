import time


class Car:
    def __init__(self, name, gb, color, delay):
        self.name = name
        self.color = color
        self.gearbox = gb
        self.engine_mode = False
        self.rpm = 0
        self.delay = delay

    def start_engine(self):
        self.engine_mode = True

    def car_break(self):
        print("Decreasing speed")

    def accelerate(self, value):
        if self.engine_mode == True:
            for i in range(value):
                time.sleep(self.delay)
                self.rpm += 1000
                print(self.rpm)

    def info(self):
        print(self.name)
        print(self.color)
        print(self.gearbox)


# Instance or Object ( Shey )
dena = Car("Dena", "Automatic", "Black", 1.7)
persia = Car("Persia", "Manual", "Pink", 1.6)

persia.start_engine()
persia.accelerate(4)
