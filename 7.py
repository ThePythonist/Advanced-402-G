def average(*args):
    try :
        return sum(args) / len(args)
    except ZeroDivisionError:
        return None


print(average())
