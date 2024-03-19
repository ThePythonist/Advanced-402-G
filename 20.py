class Human:
    def __init__(self, familyname, address, city, job):
        self.familyname = familyname
        self.address = address
        self.city = city
        self.job = job

    def talk(self):
        print("Hello")


class Student(Human):
    def __init__(self, familyname, address, city, university, fieldofstudy, job=None):
        # --- Inherited ---
        super().__init__(familyname, address, city, job)

        # --- Not Inherited ---
        self.uni = university
        self.field = fieldofstudy

    def entekhab_vahed(self):
        print("Entekhab vahed")


hamidreza = Human("Ahangar", "Tohid", "Tehran", "Trader")
amirhossein = Student("Ahangar", "W Ferdos", "Tehran", "Sharif University", "Computer Engineering")

amirhossein.entekhab_vahed()
