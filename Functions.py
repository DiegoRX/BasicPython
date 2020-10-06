def sum(a, b):
    total = a + b
    return total 

sum (45, 55)

def fullName(name, lastName, inverted=False):
    if inverted:
        return f'{lastName} {name}'
    else:
        return f'{name} {lastName}'

fullName('Diego', 'Romero')
fullName('Diego', 'Romero, inverted=True')
