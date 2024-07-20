"""Aboid 'if-else' Hell in Python with this simple trick."""
def first():
    print("first")

def second():
    print("second")

def third():
    print("third")

def default():
    print("default")

var: int = 2

if var == 0:
    first()
elif var == 1:
    second()
elif var == 2:
    third()
else:
    default()


funcs: dict = {0: first,
               1: second,
               2: third}

final = funcs.get(var, default)
final()


