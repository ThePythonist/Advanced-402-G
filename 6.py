import jdatetime as j


def show_age(birth):
    thisyear = j.datetime.now().year
    age = thisyear - birth
    print(age)


show_age(1370)
