import pandas as pd

df = pd.DataFrame({'Key': ['K0','K1','K2','K4'],
        'Name': ['Anna','Bernd','Cesar','Dana']})

for index, row in df.iterrows():
    print(row['Key'], 'gehört zu', row['Name'])