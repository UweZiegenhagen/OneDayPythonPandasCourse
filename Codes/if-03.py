def check_laenge(text):
    if len(text)>8:
        print(text, 'Länger als 8 Zeichen!', sep=': ')
    else:
        print(text, 'Kürzer oder gleich als 8 Zeichen!', sep=': ')
        
check_laenge('Köln')
check_laenge('Düsseldorf')