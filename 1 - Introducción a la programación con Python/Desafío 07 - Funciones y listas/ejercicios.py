import pandas as pd

df = pd.read_csv('athlete_events.csv')

# print(df.head())

ejercicio_1 = df.shape
# print(ejercicio_1)

ejercicio_2 = df["Games"].nunique()
# print(ejercicio_2)


ejercicio_3 = df['Season'].value_counts(normalize=True)

anoMenorSummer = df[df['Season'] == 'Summer']['Year'].min()
df4 = df[df['Season'] == 'Summer'][['Year', 'City']].sort_values(by='Year')

ejercicio_4 = df[df['Year'] == anoMenorSummer]['City'].unique()

# print(ejercicio_4)

anoMenorWinter = df[df['Season'] == 'Winter']['Year'].min()

ejercicio_5 = df.query('Year == "1924" & Season == "Winter"')["City"].unique()

# ejercicio_5 = df[(df['Year'] == "1924") & (df["Season"] == "Winter")]

# print(ejercicio_5)

ejercicio_6 = df['Team'].value_counts()[:10]
# print(ejercicio_6)

ejercicio_7 = df['Medal'].value_counts(normalize=True)
# print(ejercicio_7)

ejercicio_8 = df.query('Year == " ' + str(anoMenorSummer) +
                       '" & Season == "Summer"')['Team'].unique()
# print(ejercicio_8)
