q1 = {1:'Januar',2:'Februar',3:'März'}
q2 = {4:'April', 5:'Mai',6:'Juni'}
q3 = {7:'Juli',8:'August',9:'September'}
q4 = {10:'Oktober',11:'November',12:'Dezember'}

print(id(q1))

jahr = q1
print(id(jahr))

jahr = q1.copy()
print(id(jahr))

jahr.update(q2)
jahr.update(q3)
jahr.update(q4)

monthnames = ['January','February','March','April','May','June',
'July','August','September','October','November','December']
monthnumbers = jahr.keys()

year = dict(zip(monthnumbers,monthnames))

from pprint import pprint # bessere Ausgabe

pprint(year)
pprint(jahr)

q3.clear()
pprint(q3)