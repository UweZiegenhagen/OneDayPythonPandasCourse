s = 'Hallo Welt'
l = len(s)

while (l>0):
    temp = s[l-1]
    if temp == 'W':
        break
    print(temp)
    l-=1