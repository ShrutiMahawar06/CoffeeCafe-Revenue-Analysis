import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\shrut\OneDrive\Desktop\project unified mentor\_Coffee Roasters.xlsx - Transactions.csv")

# Calculate revenue
df['Revenue'] = df['transaction_qty'] * df['unit_price']
Total_revenue = df['Revenue'].sum()

# Top 10 products by revenue
top10_revenue = df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False).head(10)

# Draw bar chart
plt.figure(figsize=(12, 6))
plt.barh(top10_revenue.index, top10_revenue.values, color='brown')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Revenue (₹)')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('top10_revenue.png')
print("Chart saved!")

# CHART 2 - Pie chart for revenue share by category
category_revenue = df.groupby('product_category')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 8))
plt.pie(category_revenue.values, 
        labels=category_revenue.index, 
        autopct='%1.1f%%',
        colors=['brown', 'tan', 'peru', 'chocolate', 'sienna', 'wheat', 'burlywood', 'sandybrown', 'saddlebrown'])
plt.title('Revenue Share by Category')
plt.tight_layout()
plt.savefig('category_share_pie.png')
print("Pie chart saved!")

# CHART 3 - Bottom 10 products by revenue
bottom10_revenue = df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False).tail(10)

plt.figure(figsize=(12, 6))
plt.barh(bottom10_revenue.index, bottom10_revenue.values, color='red')
plt.title('Bottom 10 Products by Revenue')
plt.xlabel('Revenue (₹)')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('bottom10_revenue.png')
print("Bottom 10 chart saved!")