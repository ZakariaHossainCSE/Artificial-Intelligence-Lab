import pandas as pd
df = pd.read_csv('sales_data.csv')
total_revenue = df.groupby('Product')['Revenue'].sum()
print(total_revenue)