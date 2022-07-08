def add(a, b):
    return int(a) + int(b)

a, b = input('Enter two numbers!').split()
print('The sum is: {}'.format(add(a,b)))