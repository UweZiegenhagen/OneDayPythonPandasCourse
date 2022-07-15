d = {1:'one',2:'two',3:'three'}

print(d.keys())
print(d.values())
print(d.items())

print(d.get(4))
print(d.get(3))

for k, v in d.items():
    print(k, v)
