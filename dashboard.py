# =============================================
# AFFICIONADO COFFEE ROASTERS - DASHBOARD
# =============================================

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data
df = pd.read_csv(r"C:\Users\shrut\OneDrive\Desktop\project unified mentor\_Coffee Roasters.xlsx - Transactions.csv")

# Calculate revenue
df['Revenue'] = df['transaction_qty'] * df['unit_price']

# ---- PAGE TITLE ----
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Product Optimization & Revenue Analysis Dashboard")

# ---- KPI CARDS ----
Total_revenue = df['Revenue'].sum()
total_transactions = len(df)
total_products = df['product_detail'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹ {Total_revenue:,.0f}")
col2.metric("Total Transactions", f"{total_transactions:,}")
col3.metric("Unique Products", total_products)

# ---- SIDEBAR FILTERS ----
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df['product_category'].unique(),
    default=df['product_category'].unique()
)

store_filter = st.sidebar.multiselect(
    "Select Store Location",
    options=df['store_location'].unique(),
    default=df['store_location'].unique()
)

# ---- TOP N SLIDER ----
st.sidebar.header("Product Ranking")
top_n = st.sidebar.slider("Select Top N Products", min_value=5, max_value=20, value=10)

# Apply filters
filtered_df = df[
    (df['product_category'].isin(category_filter)) &
    (df['store_location'].isin(store_filter))
]

st.write(f"Showing {len(filtered_df):,} transactions")

# ---- CHART 1 - Revenue by Category ----
st.subheader("Revenue by Category")
category_revenue = filtered_df.groupby('product_category')['Revenue'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.barh(category_revenue.index, category_revenue.values, color='brown')
ax1.set_xlabel('Revenue (₹)')
ax1.set_title('Revenue by Category')
st.pyplot(fig1)

# ---- CHART 2 - Top N Products (uses slider) ----
st.subheader(f"Top {top_n} Products by Revenue")
top_products = filtered_df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=False).head(top_n)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh(top_products.index, top_products.values, color='sienna')
ax2.set_xlabel('Revenue (₹)')
ax2.set_title(f'Top {top_n} Products by Revenue')
st.pyplot(fig2)

# ---- CHART 3 - Revenue Share Pie Chart ----
st.subheader("Revenue Share by Category")
fig3, ax3 = plt.subplots(figsize=(8, 8))
ax3.pie(category_revenue.values,
        labels=category_revenue.index,
        autopct='%1.1f%%')
ax3.set_title('Revenue Share by Category')
st.pyplot(fig3)

# ---- CHART 4 - Bottom 10 Products ----
st.subheader("Bottom 10 Products by Revenue")
bottom10 = filtered_df.groupby('product_detail')['Revenue'].sum().sort_values(ascending=True).head(10)

fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.barh(bottom10.index, bottom10.values, color='red')
ax4.set_xlabel('Revenue (₹)')
ax4.set_title('Bottom 10 Products by Revenue')
st.pyplot(fig4)

# ---- TABLE - Product Drill Down ----
st.subheader("Product Performance Table")
product_table = filtered_df.groupby('product_detail').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Quantity=('transaction_qty', 'sum'),
    Avg_Price=('unit_price', 'mean')
).sort_values('Total_Revenue', ascending=False).round(2)

st.dataframe(product_table)

# ---- CHART 5 - Popularity vs Revenue Scatter Plot ----
st.subheader("Popularity vs Revenue (Scatter Plot)")

scatter_data = filtered_df.groupby('product_detail').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Quantity=('transaction_qty', 'sum')
).reset_index()

fig5, ax5 = plt.subplots(figsize=(12, 7))
ax5.scatter(scatter_data['Total_Quantity'], 
            scatter_data['Total_Revenue'],
            color='brown', alpha=0.7, s=100)

# Add product name labels on each dot
for i, row in scatter_data.iterrows():
    ax5.annotate(row['product_detail'], 
                (row['Total_Quantity'], row['Total_Revenue']),
                fontsize=7, alpha=0.8)

ax5.set_xlabel('Total Quantity Sold (Popularity)')
ax5.set_ylabel('Total Revenue (₹)')
ax5.set_title('Product Popularity vs Revenue')
st.pyplot(fig5)