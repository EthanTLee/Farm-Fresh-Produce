from types import SimpleNamespace

kitchen = SimpleNamespace()
kitchen.__setattr__('ingredient box', SimpleNamespace())

def add_ingredients(**kwargs):
    kitchen.__dict__['ingredient box'].__dict__.update(kwargs)

def add_empty_bowls(*args):
    for arg in args: kitchen.__setattr__(arg, SimpleNamespace())

def move(name, origin, destination):
    kitchen.__dict__[destination].__setattr__(name, kitchen.__dict__[origin].__dict__[name])
    kitchen.__dict__[origin].__delattr__(name)

def mix(*items, location, new_name):
    kitchen.__dict__[location].__setattr__(new_name, list(map(lambda n: kitchen.__dict__[location].__dict__[n], items)))
    for item in items: kitchen.__dict__[location].__delattr__(item)

def bake(bowl, function, new_name):
    result = function(kitchen.__dict__[bowl])    
    kitchen.__delattr__(bowl)
    kitchen.__setattr__(bowl, SimpleNamespace())
    kitchen.__dict__[bowl].__setattr__(new_name, result)



    