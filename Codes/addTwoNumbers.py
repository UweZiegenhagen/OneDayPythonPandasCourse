def add(a, b):
    return int(a) + int(b)

a, b = input('Geben Sie zwei Zahlen ein!').split()
print('Die Summe beträgt: {}'.format(add(a,b)))