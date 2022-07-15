monatsnamen = {1:'Januar', 2: 'Februar', 3: 'März'}
print(monatsnamen[1]) # Januar
m = monatsnamen 
print(m[1]) # Januar
monatsnamen[1] = "January"
print(monatsnamen[1]) # January
print(m[1]) # January
n = monatsnamen.copy()
monatsnamen[1] = "Janvier"
print(monatsnamen[1]) # Janvier
print(n[1]) # January