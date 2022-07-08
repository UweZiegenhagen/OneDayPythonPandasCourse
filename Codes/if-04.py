def check_length(text):
    if len(text)>8:
        print(text, 'Longer than 8 chars!', sep=': ')
    else:
        if len(text)<=5:
            print(text, 'Shorter or equal 5 chars!', sep=': ')
        else:
            print(text, 'Longer than 5, shorter than 8', sep=': ')
        
check_length('Köln')
check_length('Berlin')
check_length('Düsseldorf')