s = 'Hallo Welt'
l = len(s)

while (l>0):
    l-=1
    temp = s[l]
    if temp == 'W':
        continue
    print(temp)
    