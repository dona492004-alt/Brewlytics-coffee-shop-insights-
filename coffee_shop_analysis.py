import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("coffee_sales.csv")  # file is in repo root

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Total revenue column
df['revenue'] = df['quantity'] * df['price']

# 1. Daily revenue
daily_revenue = df.groupby('date')['revenue'].sum()
print("\nDaily Revenue:\n", daily_revenue)

# Plot daily revenue
plt.figure(figsize=(8,4))
sns.lineplot(x=daily_revenue.index, y=daily_revenue.values, marker="o")
plt.title("Daily Revenue")
plt.ylabel("Revenue ($)")
plt.xlabel("Date")
plt.show()

# 2. Top-selling drinks
top_drinks = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
print("\nTop Selling Drinks:\n", top_drinks)

plt.figure(figsize=(6,4))
sns.barplot(x=top_drinks.values, y=top_drinks.index, palette="muted")
plt.title("Top Selling Drinks")
plt.xlabel("Cups Sold")
plt.show()

# 3. Revenue by product
revenue_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Product:\n", revenue_by_product)

plt.figure(figsize=(6,4))
sns.barplot(x=revenue_by_product.values, y=revenue_by_product.index, palette="muted")
plt.title("Revenue by Product")
plt.xlabel("Revenue ($)")
plt.show()
