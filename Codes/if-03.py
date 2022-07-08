def check_length(text):
    if len(text)>8:
        print(text, 'Longer than 8 characters!', sep=': ')
    else:
        print(text, 'Shorter or equal to 8 characters!', sep=': ')
        
check_length('Köln')
check_length('Düsseldorf')