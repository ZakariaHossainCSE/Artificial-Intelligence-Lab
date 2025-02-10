import pandas as pd

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Compute total revenue per product
total_revenue = df.groupby('Product')['Revenue'].sum()

print(total_revenue)