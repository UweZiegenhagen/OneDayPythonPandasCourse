def give(**args):
    for key, value in args.items():
        print(key, value, sep=': ')


print(give(Vorname='Uwe', Nachname='Ziegenhagen'))
