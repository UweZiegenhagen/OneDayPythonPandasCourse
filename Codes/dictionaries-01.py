# -*- coding: utf-8 -*-

de_en = {'Glücklich': 'Happy', 'Baum': 'Tree'}
de_en['Freunde'] = 'Friends'

print(de_en['Baum'])
# print(de_en['Tree']) # => KeyError
'Baum' in de_en

monatsnamen = {1: 'Januar', 2: 'Februar', 3: 'März'}
print(monatsnamen[1])  # Januar

m = monatsnamen
print(m[1])  # Januar

monatsnamen[1] = "January"

print(monatsnamen[1])  # January
print(m[1])  # January

n = monatsnamen.copy()
monatsnamen[1] = "Janvier"

print(monatsnamen[1])  # Janvier
print(n[1])  # January

deutsche_monate = ['Januar', 'Februar', 'März']
englische_monate = ['January', 'February', 'March']

months = zip(deutsche_monate, englische_monate)
for k, v in months:
    print(k, v)
