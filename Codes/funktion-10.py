def gib_aus(anzahl=1, **args):
    for key, value in args.items():
        print(anzahl, key, value, sep=': ')


gib_aus(Vorname='Uwe', Nachname='Ziegenhagen')
gib_aus(anzahl=2, Vorname='Uwe', Nachname='Ziegenhagen')
