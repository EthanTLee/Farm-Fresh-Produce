from types import SimpleNamespace

kitchen = SimpleNamespace()
kitchen.ingredient_box = SimpleNamespace()

def add_ingredients(**kwargs):
    kitchen.ingredient_box.__dict__.update(kwargs)

def add_empty_bowls(*args):
    for arg in args: kitchen.__setattr__(arg, SimpleNamespace())

def move(name, origin, destination):
    kitchen.__dict__[destination].__setattr__(name, kitchen.__dict__[origin].__dict__[name])
    kitchen.__dict__[origin].__delattr__(name)

def combine(*items, location, new_name):
    kitchen.__dict__[location].__setattr__(new_name, list(map(lambda n: kitchen.__dict__[location].__dict__[n], items)))
    for item in items: kitchen.__dict__[location].__delattr__(item)


    