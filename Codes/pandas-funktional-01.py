import pandas as pd

def mach_gross(text):
    return text.capitalize()

df = pd.DataFrame({'Key': ['K0','K1','K2','K4'],
        'Name': ['anna','bernd','cesar','dana']})

print(df)

df['Nachname'] = df['Name'].apply(mach_gross)

print(df)