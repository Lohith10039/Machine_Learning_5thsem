import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [50000, 500, 1200, 10000],
    'Quantity': [10, 50, 30, 15]
}

df = pd.DataFrame(data)

df['Total Value'] = df['Price'] * df['Quantity']
high= df['Total Value']
highest_value_index = df['Total Value'].idxmax()
highest_value_product = df.loc[highest_value_index, 'Product']
overall_inventory_value = df['Total Value'].sum()

print("Updated DataFrame:")
print(df)

print("\nResults:")
print(f"Product {high}")
print(f"Product with the highest total value: {highest_value_product}")
print(f"Overall inventory value: {overall_inventory_value}")
