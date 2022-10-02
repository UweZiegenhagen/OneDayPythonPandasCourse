import math
from datetime import datetime;
now = datetime.utcnow()

applecount = 42
appleprice = 1.03

print(f'{applecount}') # string interpolation
print(f'{applecount=}') # variable name
print(f'{applecount * appleprice:.4f}') # math ops and format
print(f'{math.pi:.2f}') # number format 
print(f'{now:%d.%m.%Y}') # date format