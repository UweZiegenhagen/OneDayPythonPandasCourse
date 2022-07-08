def gib_aus(*arg, **args):
    for value in arg:
        print(value)

    for key, value in args.items():
        print(key, value, sep=': ')


gib_aus(1, 2, 3, 4, 5, Vorname='Uwe', Nachname='Ziegenhagen')
