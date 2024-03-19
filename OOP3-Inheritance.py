# class A:
#     def sayhello(self):
#         print("Hello")
#
#
# class B(A):
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()
#
# farzand.sayhello()

# -------------------------------------------

# class Father:
#     def __init__(self, familyname, address, city, job):
#         self.familyname = familyname
#         self.address = address
#         self.city = city
#         self.job = job
#
#     def sayhello(self):
#         print("Hello")
#
#
# class Child(Father):
#     def __init__(self, familyname, address, city, university, fieldofstudy, job=None):
#         # --- Inherited ---
#         super().__init__(familyname, address, city, job)
#
#         # --- Not Inherited ---
#         self.uni = university
#         self.field = fieldofstudy
#
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# ahmad = Father("Hosseini", "Ekbatan,Varzesh St", "Tehran", "Salesman")
# ramin = Child("Hosseini", "Ekbatan,Varzesh St", "Tehran", "Sharif University", "Computer Engineering", "Programmer")
#
# print(ramin.job)

# -------------------------------------------

# Without Inheritance

class Pedar:
    def __init__(self, fname="ahmadi"):
        self.familyname = fname

    def greeting(self):
        print("hello")


class Farzand:
    def __init__(self):
        self.pedar = Pedar()

    def say_goodbye(self):
        print("goodbye")


pesar = Farzand()
print(pesar.pedar.familyname)
