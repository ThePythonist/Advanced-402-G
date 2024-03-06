def myhash(entry):
    if len(str(entry)) == 1:
        return entry
    else:
        figures = [int(i) for i in str(entry)]
        entry = sum(figures)
        return myhash(entry)


print(myhash(94534))
