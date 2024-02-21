import jdatetime

d = int(input("Enter day : "))
m = int(input("Enter month : "))
y = int(input("Enter year : "))
date = jdatetime.date.fromgregorian(day=d, month=m, year=y)
print(date)
