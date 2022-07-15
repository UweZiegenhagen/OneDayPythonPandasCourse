import pandas as pd

df = pd.DataFrame({'A': ['A0','A1','A2','A3'], 
	'Net': [100, 200, 300, 400]})

df['Gross'] = df['Net'].map(lambda x: x * 1.19)

print(df)