class Person:
    def __init__(self, name, age, city, job):
        self.name = name
        self.age = age
        self.city = city
        self.job = job

    def talk(self):
        print(f"""
I'm {self.name} and I'm {self.age} years old.
I live in {self.city} and I work as a {self.job}.
""")


ali = Person("ali", 24, "qazvin", "programmer")
ali.talk()
