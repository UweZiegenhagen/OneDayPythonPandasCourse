import pandas as pd

df = pd.DataFrame({'A': ['A0','A1','A2','A3'], 
	'Country': ['DEU','USA','ARE','ESP']})

countries = { 'DEU':'Germany',
             'USA':'United States',
             'ARE':'Arabic Emirates',
             'ESP':'Spain'}

df['Country'] = df['Country'].map(countries)

print(df)