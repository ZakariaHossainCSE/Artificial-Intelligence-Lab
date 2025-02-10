import pandas as pd
df = pd.read_csv('dataset.csv')
df_filled = df.fillna(df.mean())
print(df_filled)