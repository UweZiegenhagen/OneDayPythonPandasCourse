def check_laenge(text):
    if len(text)>8:
        print(text, 'Länger als 8 Zeichen!', sep=': ')
    else:
        if len(text)<=5:
            print(text, 'Kürzer oder gleich als 5 Zeichen!', sep=': ')
        else:
            print(text, 'Länger als 5, kürzer als 8', sep=': ')
        
check_laenge('Köln')
check_laenge('Berlin')
check_laenge('Düsseldorf')