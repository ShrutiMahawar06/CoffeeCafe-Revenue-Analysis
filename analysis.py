# =============================================
# AFFICIONADO COFFEE ROASTERS - DATA ANALYSIS
# =============================================

import pandas as pd

# Loading our CSV file
df = pd.read_csv("_Coffee Roasters.xlsx - Transactions.csv")

# Let's see what's inside our data
print("=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== TOTAL ROWS AND COLUMNS ===")
print(df.shape)

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== REVENUE ===")
df['Revenue'] = df['transaction_qty'] * df['unit_price']
print (df['Revenue'])

print("\n=== TOTAL REVENUE ===")
print (df["Revenue"].sum())
Total_revenue = df["Revenue"].sum()
print(Total_revenue)

print("\n=== Revenue by category ===")
revenue_by_category = df.groupby('product_category')['Revenue'].sum().sort_values(ascending=False)
print(revenue_by_category)

print("\n=== Revenue by share of category ===")
category_share = (revenue_by_category / Total_revenue * 100).round(2)
print(category_share)

# STEP 5 - Top 10 products by revenue
print("\n=== TOP 10 PRODUCTS BY REVENUE ===")
top10_revenue = df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False).head(10)
print(top10_revenue)

# STEP 6 - Bottom 10 products by revenue
print("\n=== BOTTOM 10 PRODUCTS BY REVENUE ===")
bottom10_revenue = df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False).tail(10)
print(bottom10_revenue)

# STEP 7 - Top 10 products by quantity sold
print("\n=== TOP 10 PRODUCTS BY QUANTITY SOLD ===")
top10_quantity = df.groupby('product_detail')['transaction_qty'].sum().sort_values(ascending=False).head(10)
print(top10_quantity)

# STEP 8 - Pareto Analysis (80/20 Rule)
print("\n=== PARETO ANALYSIS ===")

# Step 1 - Revenue per product, sorted highest to lowest
product_revenue = df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False)

# Step 2 - Cumulative revenue (running total)
cumulative_revenue = product_revenue.cumsum()

# Step 3 - Cumulative percentage
cumulative_percentage = round(cumulative_revenue / Total_revenue * 100, 2)

# Step 4 - Combine into one clean table
pareto_table = pd.DataFrame({
    'Revenue': product_revenue,
    'Cumulative %': cumulative_percentage
})

# Step 5 - Mark which products fall in the 80% threshold
pareto_table['Is_Hero_Product'] = pareto_table['Cumulative %'].shift(fill_value=0) < 80

print(pareto_table)

# Step 6 - How many products make up 80% of revenue?
hero_products = pareto_table[pareto_table['Is_Hero_Product'] == True]
print(f"\nNumber of hero products driving 80% revenue: {len(hero_products)}")
print(f"Total products: {len(pareto_table)}")
print(f"\nHero products are {round(len(hero_products)/len(pareto_table)*100, 2)}% of menu")
print(f"They drive 80% of revenue")
hero_share = hero_products['Revenue'].sum() / Total_revenue * 100
rest_count = len(pareto_table) - len(hero_products)
print(f"\nHero products actually give {hero_share:.1f}% of revenue")
print(f"The other {rest_count} products give {100 - hero_share:.1f}% of revenue")

df['size'] = df['product_detail'].str.split().str[-1]
size_table = df[df['size'].isin(['Sm', 'Rg', 'Lg'])].groupby('size').agg(
    Total_Revenue=('Revenue', 'sum'),
    Variants=('product_detail', 'nunique')
)
size_table['Revenue_per_Variant'] = (size_table['Total_Revenue'] / size_table['Variants']).round(0)
print("\n=== REVENUE BY SIZE ===")
print(size_table)